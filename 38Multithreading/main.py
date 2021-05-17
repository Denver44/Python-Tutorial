# -------- MULTITHREADING ---------------

# from time import sleep
# from threading import *

# class Hello:
#     def run(self):
#         for i in range(5):
#             print("hello")


# class Hi:
#     def run(self):
#         for i in range(5):
#             print("Hi")

# # this normal as the main threading execute boh the run fuicntion and then at last bye but we want to execute boh of the at  same time the we used thrtaeding
# t1 = Hello()
# t2 = Hi()
# t1.run()
# t2.run()

# print("bye")

# --------------------------- THREADING --------------------

from time import sleep
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


# this normal as the main threading execute boh the run fuicntion and then at last bye but we want to execute boh of the at  same time the we used thrtaeding
t1 = Hello()
t2 = Hi()
# here we have to use start in place of the class function run becuase in thread fucntion there is fuction name run which execute when we call start and also we have to write run name class so that it can execute.
t1.start()
sleep(0.2)
t2.start()


# //  As here the bye will be execute by the main thread so thats we have use join as afater boh tthe rhread finsihed and join with main thfread and then bye should print that why we are using join to join there path.
t1.join()
t2.join()

print("bye")
