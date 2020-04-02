import os
import sys
import logging
import time

# https://docs.python.org/3/howto/logging.html
# https://docs.python.org/3/library/logging.html#logging.basicConfig
# log to stderr, exceptions are logged as multiple lines
# logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# ---------------------------------------------------------------

log_file_path = os.path.join(os.getcwd(), "Output", "logfile.log")

try:
    os.remove(log_file_path)
    # os.remove("output/logfile.log")
except FileNotFoundError:
    pass

# ---------------------------------------------------------------

a = 3
b = 4


def hypotenuse(a, b):
    """Compute the hypotenuse"""
    return (a ** 2 + b ** 2) ** 0.5


def tester_filter():
    time.sleep(0.1)

    kwargs = {"a": 3, "b": 4, "c": hypotenuse(3, 4)}

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("a = {a}, b = {b}".format(**kwargs))
    if logger.isEnabledFor(logging.INFO):
        logger.info("Hypotenuse of {a}, {b} is {c}".format(**kwargs))
    if logger.isEnabledFor(logging.WARNING):
        logger.warning("a={a} and b={b} are equal".format(**kwargs))
    if logger.isEnabledFor(logging.ERROR):
        logger.error("a={a} and b={b} cannot be negative".format(**kwargs))
    if logger.isEnabledFor(logging.CRITICAL):
        logger.critical("Hypotenuse of {a}, {b} is {c}".format(**kwargs))

    time.sleep(0.1)


# {LEVEL}:{LOGGER}:{MESSAGE}.
# > DEBUG:root:Hypotenuse of 3, 4 is 5.0
logging.debug("Hypotenuse of {a}, {b} is {c}".format(a=3, b=4, c=hypotenuse(a, b)))
print()

logger = logging.getLogger(__name__)
logger.setLevel(logging.NOTSET)
print("--------------- logger will log all.")
tester_filter()
print()
# DEBUG:__main__:a = 3, b = 4
# INFO:__main__:Hypotenuse of 3, 4 is 5.0
# WARNING:__main__:a=3 and b=4 are equal
# ERROR:__main__:a=3 and b=4 cannot be negative
# CRITICAL:__main__:Hypotenuse of 3, 4 is 5.0

logger.setLevel(logging.WARNING)
print("--------------- only logging WARNING, ERROR, or CRITICAL now.")
tester_filter()
print()
# WARNING:__main__:a=3 and b=4 are equal
# ERROR:__main__:a=3 and b=4 cannot be negative
# CRITICAL:__main__:Hypotenuse of 3, 4 is 5.0

# ---------------------------------------------------------------


def dump_log():
    print()
    print("--------------- logfile.log")
    # file = open("output/logfile.log", "r")
    file = open(log_file_path, "r")
    print(file.read())  # show entire contents of txt file
    print("---------------")
    print()


# define file handler and set formatter
# file_handler = logging.FileHandler("output/logfile.log")
file_handler = logging.FileHandler(log_file_path)
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

logger.setLevel(logging.NOTSET)

print("---------------")
tester_filter()
# dump_log()

# ---------------------------------------------------------------

x = 10
y = 0


def divide(x, y):
    try:
        out = x / y
    except ZeroDivisionError:
        logger.exception("Division by zero problem")
    else:
        return out


divide(x, y)
# dump_log()

# ---------------------------------------------------------------


class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)

    def format(self, record):
        result = super().format(record)
        if record.exc_text:
            result = result.replace("\n", "")
        return result


# root = logging.getLogger()
# root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
handler = logging.StreamHandler()
formatter = OneLineExceptionFormatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
# logger.removeHandler()
logger.addHandler(handler)

divide(x, y)
# dump_log()


# ---------------------------------------------------------------


class Foo(object):
    __log = logging.getLogger(__name__ + ".Foo")

    def foo(self):
        self.__log.info("foo called")


class Bar(Foo):
    __log = logging.getLogger(__name__ + ".Bar")

    def bar(self):
        self.__log.info("bar called")


bar = Bar()
bar.foo()
bar.bar()

time.sleep(0.1)

# ---------------------------------------------------------------

# class Bar(Foo):
#     def bar(self):
#         self.__log.info('bar called')

# Bar._Bar__log = logging.getLogger(__name__ + Bar.__name__) # manual name mangling


def addlogger(cls: type):
    aname = "_{}__log".format(cls.__name__)
    setattr(cls, aname, logging.getLogger(cls.__module__ + "." + cls.__name__))
    return cls


@addlogger
class Foo2(object):
    def foo2(self):
        self.__log.info("foo2 called")


@addlogger
class Bar2(Foo2):
    def bar2(self):
        self.__log.info("bar2 called")


bar2 = Bar2()
bar2.foo2()
bar2.bar2()

time.sleep(0.1)

# ---------------------------------------------------------------

dump_log()

# ---------------------------------------------------------------

main_logger = logging.getLogger("main")
main_logger.setLevel(5)

dev_logger = logging.getLogger("main.dev")

print("main effective level: ", main_logger.getEffectiveLevel())
print("dev effective level: ", dev_logger.getEffectiveLevel())
print("\n-----\n")

# ---------------------------------------------------------------

main_test_logger = logging.getLogger("main.test")
main_test_logger.setLevel(logging.WARNING)

try:
    main_test_logger.debug("debug test")
    main_test_logger.info("info test")
    main_test_logger.warning("warning test")
    main_test_logger.error("error test")
    open("/path/to/does/not/exist", "rb")
except (SystemExit, KeyboardInterrupt):
    raise
except FileNotFoundError as fnfe:
    main_test_logger.error("Failed to open file", exc_info=True)
except Exception as ex:
    main_test_logger.error("Unhandled error", exc_info=True)
