"""
1) Iterable - __iter__() or __getitem__()
2) Iterator - __next__()
3) Iteration - The process of itertation
"""


# This yield is not like the return, it is diffrent
# In place of return type yield and using __next__() we can iterate the function.

# def gen(n):
#     for i in range(n):
#         yield i

# g = gen(3)
# print(g)
# print(g.__next__()) # using next we can print the values of the generator next by next.
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

# Iter() && __next__()
# h = "dart"
# ier = iter(h)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())


# for c in h:
#     print(c)

# a = ["srk","d","r"]
# b = iter(a)
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
