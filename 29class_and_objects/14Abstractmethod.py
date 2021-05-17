# ------------------- META CLASS------------------
# from abc import ABCMeta, abstractmethod
# class shape(metaclass=ABCMeta):

#  --------- OR---------------------

from abc import ABC, abstractmethod


# We cannot make object of abstract class.
class shape(ABC):
    @abstractmethod
    def printarea(self):  # this manadatory to be define in the dreived class.
        return 0


class rectangle(shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 7
        self.breadth = 6

    def printarea(self):
        return self.length * self.breadth


r = rectangle()

print(r.printarea())
