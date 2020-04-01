# python-json-logger
#
# https://github.com/madzak/python-json-logger
# https://www.reddit.com/r/learnpython/comments/701nif/are_there_any_good_json_logging_libraries_for/
#
# Successfully installed python-json-logger-0.1.11
# Successfully installed structlog-20.1.0
#
# alternative option (not tested here):
# json-logging-python
# https://github.com/thangbn/json-logging-python
# Successfully installed json-logging-1.0.6

import os
import sys
import datetime
import logging
from pythonjsonlogger import jsonlogger

try:
    os.remove("output/json.log")
except:
    pass


def dump_log():
    print("---------- json.log")
    file = open("output/json.log", "r")
    print(file.read())  # show entire contents of txt file
    print("----------")


x = 10
y = 0


def divide(x, y):
    try:
        out = x / y
    except ZeroDivisionError:
        logger.exception("Division by zero problem")
    else:
        return out


# ----------------------------------------------------------------
# json-logging-python alternative

# import json_logging
# import logging.config
# log is initialized without a web framework name
# json_logging.ENABLE_JSON_LOGGING = True
# json_logging.init_non_web()

# logger = logging.getLogger(__name__)  # "test-logger"
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler(sys.stdout))

# logger.info("test logging statement")


# ----------------------------------------------------------------
# uses python-json-logger

logger = logging.getLogger(__name__)

# file_handler = logging.FileHandler("json.log")
# formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# handler = logging.StreamHandler()  # Or FileHandler or anything else
handler = logging.FileHandler("output/json.log")
# Configure the fields to include in the JSON output. message is the main log string itself
format_str = "%(asctime)%(levelname)%(name)%(message)"
formatter = jsonlogger.JsonFormatter(format_str)
handler.setFormatter(formatter)
logger.addHandler(handler)
# logger.setLevel(logging.DEBUG)
# Normally we would attach the handler to the root logger, and this would be unnecessary
# logger.propagate = False

# logger = logging.getLogger(__name__)  # "test-logger"
# logger.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

# logHandler = logging.StreamHandler()
# # formatter = jsonlogger.JsonFormatter()
# # logHandler.setFormatter(formatter)
# logHandler.setFormatter(jsonlogger.JsonFormatter())
# logger.addHandler(logHandler)
# # logger.addHandler(logging.StreamHandler(sys.stdout))

divide(x, y)
dump_log()
