# from https://towardsdatascience.com/are-you-using-python-with-apis-learn-how-to-use-a-retry-decorator-27b6734c3e6

import os
import logging
import random
import time
from functools import wraps

logger = logging.getLogger(__name__)


def retry(exceptions, total_tries=4, initial_wait=0.5, backoff_factor=2, logger=None):
    """
    calling the decorated function applying an exponential backoff.
    Args:
        exceptions: Exeption(s) that trigger a retry, can be a tuble
        total_tries: Total tries
        initial_wait: Time to first retry
        backoff_factor: Backoff multiplier (e.g. value of 2 will double the delay each retry).
        logger: logger to be used, if none specified print
    """

    def retry_decorator(f):
        @wraps(f)
        def func_with_retries(*args, **kwargs):
            _tries, _delay = total_tries + 1, initial_wait
            while _tries > 1:
                try:
                    log(f"{total_tries + 2 - _tries}. try:", logger)
                    return f(*args, **kwargs)
                except exceptions as e:
                    _tries -= 1
                    print_args = args if args else "no args"
                    if _tries == 1:
                        msg = str(
                            f"Function: {f.__name__}\n"
                            f"Failed despite best efforts after {total_tries} tries.\n"
                            f"args: {print_args}, kwargs: {kwargs}"
                        )
                        log(msg, logger)
                        raise
                    msg = str(
                        f"Function: {f.__name__}\n"
                        f"Exception: {e}\n"
                        f"Retrying in {_delay} seconds!, args: {print_args}, kwargs: {kwargs}\n"
                    )
                    log(msg, logger)
                    time.sleep(_delay)
                    _delay *= backoff_factor

        return func_with_retries

    return retry_decorator


def log(msg, logger=None):
    if logger:
        logger.warning(msg)
    else:
        print(msg)


def test_func(*args, **kwargs):
    rnd = random.random()
    if rnd < 0.2:
        raise ConnectionAbortedError("Connection was aborted :(")
    elif rnd < 0.4:
        raise ConnectionRefusedError("Connection was refused :/")
    elif rnd < 0.8:
        raise ConnectionResetError("Guess the connection was reset")
    else:
        return "Yay!!"


if __name__ == "__main__":
    # log to stderr, exceptions are logged as multiple lines
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

    # wrapper = retry((ConnectionAbortedError), tries=3, delay=.2, backoff=1, logger=logger)
    # wrapped_test_func = wrapper(test_func)
    # print(wrapped_test_func('hi', 'bye', hi='ciao'))

    wrapper_all_exceptions = retry(Exception, total_tries=2, logger=logger)
    wrapped_test_func = wrapper_all_exceptions(test_func)
    print(wrapped_test_func("hi", "bye", hi="ciao"))
