class Logger:
    def __init__(self):
        self.__map = dict()

    def shouldPrintMessage(self, time_stamp, message):
        if message in self.__map:
            previous_time_stamp = self.__map[message]
            if time_stamp >= previous_time_stamp + 10:
                self.__map[message] = time_stamp
                print("True")
            else:
                print("False")
        else:
            self.__map[message] = time_stamp
            print("True")


logger = Logger()
logger.shouldPrintMessage(1, "foo")
logger.shouldPrintMessage(2, "bar")
logger.shouldPrintMessage(3, "foo")
logger.shouldPrintMessage(8, "bar")
logger.shouldPrintMessage(10, "foo")
logger.shouldPrintMessage(11, "foo")
