
import logging
import logging.config
import logging.handlers

import fileConfig_test_module

def clear_handlers(logger):
    for handler in list(logger.handlers):
        print(handler)
        if handler.__class__.__name__ == "FileHandler":
            handler.flush()
            handler.close()
            logger.removeHandler( handler )
        else:
            handler.flush()
            logger.removeHandler( handler )

def clear_all_handlers(logger):
    root.handlers.clear()

def show_all_handlers(logger):
    for handler in logger.handlers:
        #print(handler.name)
        #print(handler.__class__.__name__)
        print(handler)

# no messages will appear from module fileConfig_test_module cause fileConfig
# and dictConfig will override all loggers current established, need to set
# disable_existing_loggers=False to avoid this problem.

# load the logging configuration
logging.config.fileConfig('config/logging.ini')

fileConfig_test_module.foo()
bar = fileConfig_test_module.Bar()
bar.bar()

root = logging.getLogger()
show_all_handlers(root)
print("Before: {} handlers".format(len(root.handlers)))
clear_all_handlers(root)
print("After: {} handlers".format(len(root.handlers)))
show_all_handlers(root)


logger = logging.getLogger(__name__)

# The logging.fileConfig and logging.dictConfig function’s default behavior is
# to disable existing loggers when they are called.
#
# load config from file
# logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
# or, for dictConfig
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,  # this fixes the problem
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'INFO',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        }
    }
})

logger.info('It works!')

