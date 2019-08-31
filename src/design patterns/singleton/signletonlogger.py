import datetime
import os


class Logger(object):
    log_file = None

    @staticmethod
    def instance():
        if "_instance" not in Logger.__dict__:
            Logger._instance = Logger()
        return Logger._instance

    def open_log(self, path):
        self.log_file = open(path, mode="w")
        print(os.path.abspath(path))

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = '%s : %s ' % (now, log_record)
        self.log_file.writelines(record)

    def close_log(self):
        self.log_file.close()


logger = Logger.instance()
logger.open_log("my.log")
logger.write_log("Loggin wth classic Singleton patter")
logger.close_log()


with open("my.log", 'r') as f:
    for line in f:
        print(line)
