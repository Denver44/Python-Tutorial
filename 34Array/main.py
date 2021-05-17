# ------------------- ARRAY 01-------------------
# import array as ar
# val = ar.array('i', [5, 6, 7, 8, 9, 10])
# for i in val:
#     print(i)


# --------------  ARRAY 02 ------------------------
# import array as ar
# arr = ar.array('i', [])

# n = int(input("Enter the size of the array u want"))

# for i in range(n):  # taking inout from the user
#     x = int(input("Enter the next value"))
#     arr.append(x)

# val = int(input("Enter the value u r searching "))  # searching for a value.
# k = 0
# for i in arr:
#     if i == val:
#         print("The index of the ", i, " in the array is ", k+1)
#         break

#     k += 1


# ---------------------------------- Array 03--------------------------
import array as arr

size = int(input())

arr1 = arr.array('i', [])
i = 0

while i < size:
    a = int(input())
    arr1.append(a)
    i += 1

for i in arr1:
    print(i)

# ----------------- NUMPY for Array 04------------- N(dimension) Matrix
# # Python program for
# # Creation of Arrays
# import numpy as np

# # Creating a rank 1 Array
# arr = np.array([1, 2, 3])
# print("Array with Rank 1: \n", arr)

# # Creating a rank 2 Array here we have to write the row and column in a single list and then eac row speated by ,
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])
# print("Array with Rank 2: \n", arr)

# # Creating an array from tuple
# arr = np.array((1, 3, 2))
# print("\nArray created using "
#       "passed tuple:\n", arr)
