import datetime
import os
from singletonfinxingsrp import Singleton

class Logger(Singleton):
    log_file = None

    def __init__(self, path):
        if self.log_file is None:
            self.log_file = open(path, mode="w")

    # def open_log(self, path):
    #     self.log_file = open(path, mode="w")
    #     print(os.path.abspath(path))
    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record =  '%s : %s ' % (now, log_record)
        self.log_file.writelines(record)

    def close_log(self):
        self.log_file.close()


# logger = Logger("my.log")
# logger.write_log("Loggin wth classic Singleton patter")
# logger.close_log()


# with open("my.log", 'r')  as f:
#     for line in f:
#         print(line)
