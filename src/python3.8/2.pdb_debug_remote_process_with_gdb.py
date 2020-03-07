from urllib.request import urlopen
import time
name="Sudeep Patel"
print(name)
time.sleep(1000000)
url = 'https://localhost:9091'
response = urlopen(url)
print(response.read())

# debugging with gdb
# nc -l 9091 to start server
# gdb python 2167
#  sudo apt-get install python3-dbg python3-dev
# zcat /usr/share/doc/python3.6/gdbinit.gz >> ~/.gdbinit

# gdb -p <Processid>
# py-bt








# Basically the above code snippet tries to make a GET request to the above url and print it’s response. Please save the above few lines of code in a file and execute it. In this case, the printed output would be the HTML page of Google.

# In another terminal, please type the following command

# $ nc -l 9091

# If you’re not aware of nc command, you can read about it here: https://en.wikipedia.org/wiki/Netcat. But simply put, we are starting a simple web server with nc command.

# We will change the python code we wrote earlier to make it problematic. Instead of Google, I’ll try to walk through the scenario with the example web server we started.

# import urllib2
# url = 'https://localhost:9091'
# response = urllib2.urlopen(url)
# print response.read()

# Now if we start the same python process, it wouldn’t print a thing, but keep on running… If you had started this process from foreground, yes, you can kill it. But imagine this running in your production instance where the job runs in background and you don’t have nothing in logs printed but the process is running according to linux. We will start debugging now. For that we need gdb. Please install it for the linux variant you are using https://wiki.python.org/moin/DebuggingWithGdb.

#     First find the process id (pid) of our running python process.
#     In my case it was 2167, now let’s attach the gdb to this python process. gdb python 2167 This command will let you connect to the python process.
#     In the gdb console, py-bt . This command should give you the python frame which the process in executing right now (where it is stuck, in our case). If you go to the bottom of the frame, it should give our program’s statement

# 4. It’s stuck in the line, where it is trying to open a https connection to the given url. Basically, our server doesn’t know how to respond to a HTTPS connection(nc just listens on the port and nothing else) and our awesome python client we wrote, waits for the server to accept the SSL handshake almost indefinitely. If you try to do, py-list in the gdb shell, it would give the exact statement which is trying to execute
# Did you see the location?? Still trying to do handshake, Duh!

# 5. Some more commands which would be useful, py-locals . This gives all the local variables in the frame in which it is currently executing.
# Timeout is none (facepalm!!)

# 6. So, the main problem was we never set any timeout for this connection and hence our process was struck in the initial handshake itself forever. This can also happen in many cases like, for example, It could be waiting for you to provide a client certificate or stuck in a certificate validation that never completes. It is always best practice to set timeout for all API calls. I repeat, set timeout for all API calls.

# Now let’s modify our code to include timeout. And it’s successfully logs that the SSL handshake timed out

# import urllib2
# url = 'https://localhost:9091'
# response = urllib2.urlopen(url, timeout=5)
# print response.read()

# So, in summary

#     GDB can be used debug a python process and you can also attach it to an already running python process.
#     Useful list of commands for GDB python debugger

#     py-bt — Get stack trace of the python process
#     info threads — If one process has more than one thread, you can find the list of all threads executing.
#     py-list — Find out the code which the current thread is executing
#     py-down — Select and print the python stack frame called by this one (if any)
#     py-up — Select and print the python stack frame that called this one (if any)
#     py-locals — Get all python local variables in the current frame
#     py-print — Look up the given python variable name