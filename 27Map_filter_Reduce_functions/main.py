numbers = ["14", "4", "5"]


# for i in range(len(numbers)):
    # numbers[i] = int(numbers[i]) + 10
# print(numbers)


#------------------------ Map function-------------------------#

# numbers = list(map(int, numbers))
# numbers[2] = numbers[2]+1
# print(numbers)


# ------------ the first agrs in which we want to convert in datatypes or in fucntion -------------------

num = [2, 3, 4, 5, 6, 7]
square = list(map(lambda a: a*a, num)) 
print(square)
print(num)

#--------------------02--------------
# def square(a):
#     return a * a


# def cube(a):
#     return a * a * a

# func = [square, cube]

# for i in range(5):
#     val = list(map(lambda x: x(i), func))
#     print(val)


# ---------------- FILTER------------------#
list1 = [1,2,3,4,5,6,7,8,9]
def is_greater(i):
    return i<=8

greaterthan = list(filter(is_greater,list1))
print(greaterthan)

#--------------- REDUCE-----------------#
from functools import  reduce
list3 =[1,2,7,10]
# num = reduce(lambda x,y:x+y,list3)
num = reduce(lambda x,y:x*y,list3)
print(num)
