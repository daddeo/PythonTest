def logger(func):
    def wrapper():
        print("Logging execution...")
        func()
        print("Logging complete.")

    return wrapper


@logger
def sample():
    print("-- inside sample")


sample()
