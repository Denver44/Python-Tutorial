# --------------------------------- DATA TYPES in PYTHON -----------------------------------
var1 = "54"  # string
var2 = 32  # Integer
var3 = 36.7  # Float

# -------------------------------- type() this function will return the type of your data Type.-----------------------------------
print(type(var1))
print(type(var2))
print(type(var3))
print(str(int(var1) + var2))
print(100 * "Hello world\n")

# -------------------------------------To Take Input From user.---------------------------------------------------
# NOTE : When we take input from user in python the input is always in string so typecaste it as per your need
print("Enter something user")
a = input()  # To take Input from User we have to use Input Function.
print("you have Enterd ", a)
print("Datatype is ", type(a))

# --------------------------- Typecasting ---------------------
# str()
# int()

print("Enter something user")
a = int(input())  # Typecasting to int
print("you have Enterd ", a)
print("Datatype is ", type(a))
