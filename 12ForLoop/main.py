#  ---------------------- FOR LOOP --------------------------
list1 = [["Garry", 1], ["Larry", 2],
         ["Carry", 6], ["Marry", 250]]
dict1 = dict(list1)  # typecasted in dictionary from list.
print(dict1)


for key in dict1:  # if we pass on args then it will be taken as key.
    print(key)


# if we pass two args then one key and anoither will be value.
for key, value in dict1.items():
    print(key, "=>", value)


# List Printing
items = [int, float, "44", 5, 3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    print(item, end=" ")

print()


# here the int and float is not string thats why we convert them string and then check it.
for item in items:
    if str(item).isnumeric() and int(item) > 6:
        print(item, end=" ")
