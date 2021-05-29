m = int(input())
mdata = set(map(int,input().split()))
n = int(input())
ndata = set(map(int,input().split()))

l1 = list(mdata.difference(ndata))
l2 = list(ndata.difference(mdata))

l3 = []
for i in range(len(l1)):
    l3.append(l1[i])
for i in range(len(l2)):
    l3.append(l2[i])
l3.sort()
for i in range(len(l3)):
    print(l3[i])