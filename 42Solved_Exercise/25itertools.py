from itertools import product

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))



l3 = list(product(l1,l2))

for i in range(len(l3)):
    print(l3[i],end=" ")
