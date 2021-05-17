
#---------- GENERATORS*----------------
# for genrators we use () parenthesis.

even = (i for i in range (1,10) if i %2 == 0)

print(type(even))
print(even.__next__())
print(even.__next__())
print(even.__next__())
print(even.__next__())