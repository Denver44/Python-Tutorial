

# 1) --------------To get address of variable use this Function =>   id(variable_name).----------------------
# num = 5
# print(id(num)) #here the id(variable_name) gives the address of the num store in the memeory


# 2)--------------------- short way to assign Values to our variable----------------------------
# a, b,c,d = 5, 6,7,8
# print(a)
# print(b)
# print(c)
# print(d)

# 3)------------------------ Decimal, octal hexa and binary Conversion--------------------------------
# print(bin(25))  # Printing decimal to bin
# print(0b0101)   # Printing Binary number to Decimal
# print(oct(25))  # Printing Decimal number to Octal
# print(hex(10))  # Printing Decimal number to Hexa Decimal
# a = bin(8) # We can Store a Binary Number in A Variable and then we can Print it Later.
# print("Binay of 8 -> ", a)


# 4)----------------------- Swap Variables Old Technique.-------------------------------------
a, b = 1, 8
print(a, b)
temp = a  # Temp is Helper Variable.
a = b
b = temp
print(a, b)
# -------------------------- Swapping variables Values  in Python Superfast Technique------------------------------------------
c, d = 5, 4
print(c, d)
c, d = d, c
print(c, d)


# 5 ----------------------To Print a Power Form use   ** (double asterik mark)--------------------------------
print(2 ** 2)


# 6 ----------------------------- IMPROTANT CONCEPT OF  == vs is ---------------------------------------
# == - value equality - Two objects have the same value
# is - reference equality - Two references refer to the same object


# Task:
a = [6, 4, "34"]
b = [6, 4, "34"]
print(b == a)
print(b is a)
# Reason of false because both are on different address.
print(id(a))
print(id(b))

a = 5
b = a
print(b is a)
# Reason of true because both have a same address and b is like alias for a.
print(id(a))
print(id(b))

# but now check
b = 55
print(b is a)
# Reason of false because both are on different address as we change the value of b from 5 to 55.
print(id(a))
print(id(b))
