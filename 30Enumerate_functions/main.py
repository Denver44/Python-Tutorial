list = ["Pepsi", "Vimbar", "vimgel", "fan", "harpic"]

i = 0
for items in list:
    if i % 2 == 0:
        print(items, end=" ")
    i += 1
print()

# -------------------------------Enumerate function-------------------------------------------

for index, item in enumerate(list):
    if index % 2 == 0:
        print(index, " ", item)

print("Enumerate list is used for enumrating the  list and index.")
for index, item in enumerate(list):
    print(index, " ", item)
