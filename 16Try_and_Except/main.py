

# ----------------------------------- TRY AND EXCEPT -------------------------------

a = input()
b = input()

try:
    print("The sum is ", int(a) / int(b))
except Exception as error:  # program will not crash from here.
    print(error)

print("This is very important the Try and except help us to execute me if any error take place ")
# For c++ programmer we have catch there but here we have except.


# ----------------------- Without try and Excpet ----------------

a = input()
b = input()
# program will be crash from here if any error took place
print("The sum is ", int(a) / int(b))
print("This is very important the Try and except help us to execute me if any error take place ")
