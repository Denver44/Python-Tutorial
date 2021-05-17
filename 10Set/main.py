# --------------------------------------------- SET------------------------------------
s = set()  # declare a set  using set().
print(type(s))

l = [1, 2, 3, 4]
s1 = set(l)  # list l converted into set.
print(type(s1))
s1.add(1)
s1.add(2)
print(s1)
s1.remove(2)
print(s1)

s = {1, 2, 3, 4, 1, 2, 3, 4}
print(type(s))
print(s)
s2 = s.copy()  # to make a copy of set.
s.add(5)  # to add items in set.
s.clear()  # to clear the set
print(s2)
print(s.difference(s2))  # to find diffrence between two set.
