# python-json-logger, structlog
#
# https://github.com/madzak/python-json-logger
# https://blog.sneawo.com/blog/2017/07/28/json-logging-in-python/
# http://www.structlog.org/en/stable/
# https://www.reddit.com/r/learnpython/comments/701nif/are_there_any_good_json_logging_libraries_for/
#
# Successfully installed python-json-logger-0.1.11
# Successfully installed structlog-20.1.0
#
# processors:
# https://github.com/hynek/structlog/wiki/Third-Party-Extensions
#
# structlog-pretty
# Successfully installed pygments-2.6.1 structlog-pretty-0.1.1

import os
import datetime

import logging.config
from pythonjsonlogger import jsonlogger

import structlog

# from structlog import configure, processors, stdlib, threadlocal, get_logger

try:
    os.remove("/output/log.json*.*")
except:
    pass


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

# ----------------------------------------------------------------
# adds in structlog

# logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

# "file": {
#     "class": "logging.handlers.RotatingFileHandler",
#     "formatter": "json",
#     "filename": "log.json",
#     "mode": "w",
#     "maxBytes": 1024,
#     "backupCount": 1,
#     "level": "DEBUG",
# },

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "format": "%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s",
                "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            }
        },
        "handlers": {
            "file": {
                "class": "logging.FileHandler",
                "formatter": "json",
                "filename": "output/log.json",
                "mode": "w",
            },
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "json",
                "level": logging.INFO,
            },
        },
        "loggers": {"": {"handlers": ["console", "file"], "level": logging.DEBUG}},
    }
)

# on formatter: "datefmt": "%A, %B %e, %Y at %I:%M %p", or # %m-%d %H:%M
# %(message)s %(lineno)d %(pathname)s
#        "loggers": {"": {"handlers": ["console", "file"], "level": "DEBUG"}},
#            "__main__": {"handlers": ["json_console"], "level": logging.DEBUG},

# LOGGING_CONFIG = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'standard': {
#             'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
#         },
#     },
#     'handlers': {
#         'default': {
#             'level': 'INFO',
#             'formatter': 'standard',
#             'class': 'logging.StreamHandler',
#             'stream': 'ext://sys.stdout',  # Default is stderr
#         },
#         'default': {
#             'level': 'INFO',
#             'formatter': 'standard',
#             'class': 'logging.FileHandler',
#             'stream': 'log.json',  # Default is stderr
#         },
#     },
#     'loggers': {
#         '': {  # root logger
#             'handlers': ['default'],
#             'level': 'WARNING',
#             'propagate': False
#         },
#         'my.packg': {
#             'handlers': ['default'],
#             'level': 'INFO',
#             'propagate': False
#         },
#         '__main__': {  # if __name__ == '__main__'
#             'handlers': ['default'],
#             'level': 'DEBUG',
#             'propagate': False
#         },
#     }
# }

# logging.config.dictConfig(DEFAULT_LOGGING)


# def add_timestamp(_, __, event_dict):
#     event_dict["timestamp"] = datetime.datetime.utcnow()
#     return event_dict
#        add_timestamp,
#        structlog.processors.JSONRenderer(indent=1, sort_keys=True),

structlog.configure(
    context_class=structlog.threadlocal.wrap_dict(dict),
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_log_level_number,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.stdlib.render_to_log_kwargs,
    ],
)

#        structlog.processors.JSONRenderer(indent=2, sort_keys=True),

logger = structlog.getLogger(__name__)
logger.info("event", some_param=42)

divide(x, y)


def handler():
    log = structlog.getLogger(__name__)
    log = log.bind(correlationid="foobar")
    log.info("test", {"field": "value"})
    nestedfunction()
    try:
        this_will_fail
    except:
        logging.exception("Something went wrong", {"status": "failed"})
        # raise


def nestedfunction():
    logging.info("logging within a function", {"field": "value"})


handler()

logger.debug("Test debug message.")
logger.info("Test info message.")
logger.warning("Test warning message.")
logger.error("Test error message.")
logger.critical("Test critical message.")
