
x = int(input())
y = int(input())
z = int(input())
n = int(input())

list1 = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i < x and j < y and k < z and (i+j+k) != n]

# for i in range(x):
#     for j in range(y):
#         for k in range(z):
#             if i < x and j < y and k < z and i+j+k != n:
#                 list1.append([i, j, k])


print(list1)



 # First wat you want to append
 # second iteration
 # third Condition