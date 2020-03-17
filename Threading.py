from time import sleep
from threading import *


class SayYes(Thread):
    def run(self):
        for i in range(5):
            print("Yes")
            sleep(1)  # in seconds


class SayNo(Thread):
    def run(self):
        for i in range(5):
            print("No")
            sleep(1)  # in seconds


thread1 = SayYes()
thread2 = SayNo()

thread1.start()
sleep(0.2)  # in seconds
thread2.start()

thread1.join()  # wait on thread 1 to finish
thread2.join()  # wait on thread 2 to finish

# after both threads finish then main thread can continue
print("end")
