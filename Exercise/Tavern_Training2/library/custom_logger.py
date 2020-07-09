import inspect
import logging


def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    if not logger.handlers:
        # By default, log all messages
        logger.setLevel(logging.DEBUG)

        fileHandler = logging.FileHandler("automation.log", mode='a')
        fileHandler.setLevel(logLevel)

        formatter = logging.Formatter('%(process)d - %(asctime)s - %(module)s:%(lineno)s - %(funcName)s '
                                      '- %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
    return logger
