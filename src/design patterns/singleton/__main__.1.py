from logger_meta import Logger

logger = Logger("my.log")
logger.write_log("Loggin wth classic Singleton patter")

logger2 = Logger("***ignored****")
logger2.write_log("another wth classic Singleton patter")

logger.close_log()


with open("my.log", 'r')  as f:
    for line in f:
        print(line)