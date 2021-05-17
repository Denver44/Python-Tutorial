# ------------------------------------------ F strings--------------------------------------------
name, dob = "Durgesh",  55555
a = "this is %s %d" % (name, dob)
print(a)
# OR
print("Hello baby I am %s born on %d" % (name, dob))


a = f"this is {name} {dob}"  # this is called f-string
print(a)


# ------------------------- Another way to print ------------------------------
a = "This is {1} {0}"
b = a.format(name, dob)
print(b)
