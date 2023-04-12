import inspect
import logging


filename = str(inspect.stack())
print(filename)
logger = logging.getLogger(filename)
filehandler = logging.FileHandler("log.log")
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
logger.setLevel(logging.DEBUG)
logger.info("hiiiiiiiiiiiiiiiiiiiiiiiiiii")
