import re
import time


# define the name of the file to read from
filename = r"D:\ELK\logstash-6.5.4\config\php_extracted.txt"

massagedLog = r"D:\ELK\logstash-6.5.4\config\massagedLog.csv"

massagedLogPtr = open(massagedLog, "w")
CRLF = "\r\n"

def writeToNewLog(writefile,data,EOF ):
        writefile.write(data +  "\r")
    # else:
    #     writefile.write(data) 


print(filename)
with open(filename, 'r') as filehandle:  
    counter = 0
    line1 = "" 

    for line in filehandle:
        # print(line)
        if re.match('^(-)+', line):
            # print(counter, line)
            # time.sleep(2)
            # print((line1.strip()))
            # print("Line...:", line)         
            # print("main:", line)
            # time.sleep(5)
            if line1 != "":
                writeToNewLog(massagedLogPtr, line1[0:len(line1) - 1], CRLF)
                line1 = ""
                line1  = line.replace('-', ' ').strip()
                 
        else:
            # print("else:" , line)
            # time.sleep(5)

            line = line[0:len(line) - 1]
            if line[0:6] == "Error:":
                # print("Error:")
                # time.sleep(2)
                line = '"' + line
            elif line[0:9] == "Software:":
                # print("Software:")
                # time.sleep(2)
                line = line + '"'
            else:
                line = '"' + line + '"'

            
            line1 = line1 + ',' + line
                
            # print(line1)
            # time.sleep(3)

massagedLogPtr.close()

