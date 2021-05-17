def add(x,y):
    return  x + y

nums = [5,85]
nums2 = {'x' :5 ,'y' : 15}
print(add(**nums2)) # dict use **
print(add(*nums))  # unless use *

def multiply(name ,*args):
    tot = 1
    for arg in args:
        tot = tot * arg
    print(name,end=" ")
    return (tot)

num = [5,5,5]
print(multiply(num)) # here it is pass as tupele and become tuptl of tuple in function
print(multiply("Total Value",*num ))

# ----------------------------------------- OR------------------------

def mul(*args , n):
    tot = 1
    for arg in args:
        tot = tot * arg
    print(n,end=" ")
    return (tot)

num = [5,5,5]
print(multiply(num)) # here it is pass as tupele and become tuptl of tuple in function
print(mul(*num , n="toatl value"))