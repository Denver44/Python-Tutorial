import array as arr

size = int(input())

arr1 = arr.array('i', [])
i = 0
number_string = input()
list1 = number_string.split(" ")

while i in range(size):
    a = int(list1[i])
    arr1.append(a)
    i = i+1


arr1.reverse()
for i in arr1:
    print(i, end=" ")
