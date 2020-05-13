# python-json-logger, structlog
#
# https://github.com/madzak/python-json-logger
# https://blog.sneawo.com/blog/2017/07/28/json-logging-in-python/
# http://www.structlog.org/en/stable/
# https://www.reddit.com/r/learnpython/comments/701nif/are_there_any_good_json_logging_libraries_for/
#
# Successfully installed python-json-logger-0.1.11
# Successfully installed structlog-20.1.0

# import datetime
import logging

# import logging.config
import os
import sys

from pythonjsonlogger import jsonlogger
import structlog

from log_entry_processor import LogEntryProcessor

# ----------------------------------------------------------------

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
# adds in structlog

# logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))


# debug = os.environ.get('DEBUG', 'false') != 'false'
debug = True
logging.basicConfig(
    level="DEBUG" if debug else "INFO", stream=sys.stdout, format="%(message)s"
)

# http://stevetarver.github.io/2017/05/10/python-falcon-logging.html
# could also define the array as such and assign "processor=chain"
use_prod = False
# if os.getenv('LOG_MODE', 'JSON') == 'LOCAL':
if use_prod == False:
    chain = [
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S.%f"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.dev.ConsoleRenderer(),
    ]
else:
    chain = [
        LogEntryProcessor.add_app_info,
        LogEntryProcessor.add_logger_name,
        structlog.stdlib.add_log_level,
        LogEntryProcessor.add_timestamp,
        LogEntryProcessor.censor_password,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        LogEntryProcessor.cleanup_keynames,
        structlog.processors.JSONRenderer(),
    ]

structlog.configure(
    processors=chain,
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)


# structlog.configure(
#     context_class=structlog.threadlocal.wrap_dict(dict),
#     logger_factory=structlog.stdlib.LoggerFactory(),
#     wrapper_class=structlog.stdlib.BoundLogger,
#     processors=[
#         structlog.stdlib.filter_by_level,
#         structlog.stdlib.add_logger_name,
#         structlog.stdlib.add_log_level,
#         structlog.stdlib.add_log_level_number,
#         structlog.stdlib.PositionalArgumentsFormatter(),
#         structlog.processors.TimeStamper(fmt="iso"),
#         structlog.processors.StackInfoRenderer(),
#         structlog.processors.format_exc_info,
#         structlog.processors.UnicodeDecoder(),
#         structlog.stdlib.render_to_log_kwargs,
#     ],
# )


logger = structlog.getLogger(__name__)
logger.info("event", some_param=42)

divide(x, y)
# dump_log()


def handler():
    log = structlog.getLogger(__name__)
    log = log.bind(correlationid="foobar")
    log.info("test", {"field": "value"})
    nestedfunction()
    try:
        this_will_fail
    except:
        log.exception("Something went wrong", {"status": "failed"})
        # raise


def nestedfunction():
    logger.info("logging within a function", {"field": "value"})


handler()
# dump_log()

logger.debug("Test debug message.")
logger.info("Test info message.")
logger.warning("Test warning message.")
logger.error("Test error message.")
logger.critical("Test critical message.")
