s = input()

# a = ' '.join( i.capitalize() for i in s.split(' '))
# print(a)


# 2nd method
 # EVery titile will be capitialize
# print(s.title())

# 3rd method
import string

print(string.capwords(s))

# or

print( ' '.join( i.capitalize() for i in s.split(' ')))