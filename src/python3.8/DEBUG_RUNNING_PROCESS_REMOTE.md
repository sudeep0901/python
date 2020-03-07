debugging with gdb
nc -l 9091 to start server
gdb python 2167
sudo apt-get install python3-dbg python3-dev
zcat /usr/share/doc/python3.6/gdbinit.gz >> ~/.gdbinit

gdb -p <Processid>
py-bt
