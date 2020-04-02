import logging
import logging.handlers
import os


x = 10
y = 0


def divide(x, y):
    try:
        out = x / y
    except ZeroDivisionError:
        logging.exception("Division by zero problem")
    else:
        return out


try:
    os.remove("output/unicode.log")
except:
    pass

handler = logging.handlers.WatchedFileHandler(
    os.environ.get("LOGFILE", "output/unicode.log")
)
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

divide(x, y)

print("---------- output/unicode.log")
file = open("output/unicode.log", "r")
print(file.read())  # show entire contents of txt file
print("----------")
