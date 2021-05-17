
# To summarise the difference.
# Mutable objects :  can change their state or contents. These are of type list, dict, set . Custom classes are generally mutable.
# Immutable objects can’t change their state or content. These are of in-built types like int, float, bool, string, unicode, tuple. In simple words, an immutable object can’t be changed after it is created.


# Concept of Mutable.
l2 = l1 = [1, 2, 3, 4]
print(l1[0])
print(l1[1])
print("Address of 0th index ", id(l1[0]))
print("Address of 1st index ", id(l1[1]))
print("Address of 2nd index ", id(l1[2]))
l1[0] = l1[1]
print(l1[0])
print(l1[1])
print("Address of 0th index ", id(l2[0]))# As now both the index have same value so now both will point to same address
print("Address of 1st index ", id(l2[1]))
print("Address of 2nd index ", id(l2[2]))


# MUTEABLE it doesnt return anything
l1 = [1, 5, 6]
print(l1)
l2 = l1.append(55)
print(l1)
print(l2)

# IMUTEABLE it return with update value.
s = "DURGESH"
ns = s + 'RAI'  # it return us new string
print(s)
print(ns)

# Address
lst = [1, 2, 3]
lst2 = lst
print(id(lst), id(lst2))
lst2.append(99)
print(id(lst), id(lst2))

str1 = "abcd"
str2 = str1
print(id(str1), id(str2))
str1 += '55'
print(id(str1), id(str2))
