
# ---------------------------- Fibonacci series using Generator **********
# def fib(n):
#     a = 0
#     b = 1
#     sum = 0
#     for i in range(2,n+1):
#         sum = a+ b
#         a = b
#         b= sum
#         yield sum
#
#
# g = fib(10)
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# ----------------- Factorial series using Generator **********
def fact(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
        yield sum


f = fact(5)
print(f.__next__())
print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
