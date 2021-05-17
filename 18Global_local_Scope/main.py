# ---------------------------------- GLOBAL AND LOCAL SCOPE-----------------------------
l = 10  # Global Variable


def function1(n):
    # l = 5  # Local Scope
    m = 8  # Local
    global l
    # to chnage the Global Variable we have to define global varbalbe in our function with keyword gobal and Variable name.
    l = l + 45  # now we can change our global variable through our fucntions.
    print(l, n)


print("Before going to function value of gloabl variable l is :", l)
function1("Denver")
print("After coming from function value of gloabl variable l is :", l)
print(l)

# --------------------------------- Example 02 ----------------------------------------

x = 89


def harry():
    x = 20

    def rohan():
        global x  # as it will only affect the global variable.
        # if there is no x then it will created a new x or if there any x it will chnage it value.
        x = 88
    print("before calling rohan()", x)
    # here the global value only afffcet the global variable not the local variable inside a function.
    rohan()
    print("after calling rohan()", x)


print(x)
harry()
print(x)
