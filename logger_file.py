import logging
import logging.config
import os

try:
    os.remove("output/testfile1.log")
    os.remove("output/testfile2.log")
    os.remove("output/testfile3.log")
except:
    pass

# -----------------------------------------------------

# format_string = "%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s"
# logging.basicConfig(
#     filename="output/testfile1.log", format=format_string, level=logging.DEBUG,
# )
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

# -----------------------------------------------------

format_string = "%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s"
# log_format = "%(asctime)s %(filename)s: %(message)s"
logging.basicConfig(
    filename="output/testfile1.log", format=format_string, datefmt="%Y-%m-%d %H:%M:%S"
)
root = logging.getLogger()
root.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(name)s : %(levelname)s : %(message)s")
consoleHandler.setFormatter(formatter)
root.addHandler(consoleHandler)

root.info("information message")

error_message = "authentication failed"
root.error(f'error: "{error_message}"')

# -----------------------------------------------------

logging.config.fileConfig(
    "config\\test1.ini", defaults={"logfilename": "output/testfile2.log"}
)
logger = logging.getLogger("dev")

logger.debug("Test debug message.")
logger.info("Test info message.")
logger.warning("Test warning message.")
logger.error("Test error message.")
logger.critical("Test critical message.")

handler = logger.handlers[0].level = logging.INFO
handler = logger.handlers[1].level = logging.WARNING

logger.debug("Test debug message.")
logger.info("Test info message.")
logger.warning("Test warning message.")
logger.error("Test error message.")
logger.critical("Test critical message.")

# -----------------------------------------------------

vals = [1, 2]

try:
    print(vals[4])
except Exception as e:
    logger.error("exception occurred", exc_info=True)
