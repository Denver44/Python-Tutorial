#  Normal way to send varaiables in a function

def fun1(a, b, c, d, e):
    print(a, b, c, d, e)


fun1(1, 2, 3, 4, 5)

# ----------- *args and **kwars -------------
# Normal variables should be at left most then * and last **.
# the *args take arguments as tuple.
# the **kwargs take arguments as dict.

# Example1
def fun2(*a):
    for i in a:
        print(i, end=" ")


fun2(1, 2, 3, 4, 5)


# Example2
def fun(*args, **kwargs):
    for i in args:
        print(type(args), i)
    for key, value in kwargs.items():
        print(type(kwargs), f"the name is ", {
              key}, "and birth of month is ", {value})


list1 = [1, 2, 5, 8]
list1.append("Vishal")
list1.append("geeta")
list1.append("Priya")
list1.append("Pooja")

dict = {"durgesh": "april", "Vishal": "april"}

fun(*list1, **dict)
