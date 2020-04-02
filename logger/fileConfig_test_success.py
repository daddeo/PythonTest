import logging
import logging.config
import logging.handlers

import logger_fileConfig_test_module

# no messages will appear from module logger_fileConfig_test_module cause fileConfig
# and dictConfig will override all loggers current established, need to set
# disable_existing_loggers=False to avoid this problem.

# load the logging configuration
logging.config.fileConfig("config/logging.ini", disable_existing_loggers=False)

# Loggers are held in a hierarchy by a logging.Manager instance. You can interrogate the
# manager on the root logger for the loggers it knows about.
# Calling getLogger(name) ensures that any placeholder loggers held by loggerDict are
# fully initialized when they are added to the list.
#
loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
# [<Logger logger_fileConfig_test_module (DEBUG)>]
print(loggers)

logger = logging.getLogger()
print(logger.propagate)  # True
print(logger.disabled)  # False
print(logger)  # <RootLogger root (DEBUG)>
logger2 = logging.getLogger("logger_fileConfig_test_module")
print(logger2.propagate)  # True
print(logger2.disabled)  # False
print(logger2)  # <Logger logger_fileConfig_test_module (DEBUG)>
# <StreamHandler <stdout> (DEBUG)>
for handler in logger.handlers:
    print(handler)

logger_fileConfig_test_module.foo()
bar = logger_fileConfig_test_module.Bar()
bar.bar()
