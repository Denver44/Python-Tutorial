s = input()
list = [i.isalnum() for i in s]
list1 = [i.isalpha() for i in s]
list2 = [i.isdigit() for i in s]
list3 = [i.islower() for i in s]
list4 = [i.isupper() for i in s]
print(any(list))
print(any(list1))
print(any(list2))
print(any(list3))
print(any(list4))


# any will return if any one value is true
# all will return if all value is true