m = int(input())
mdata = set(map(int,input().split()))
n = int(input())
ndata = set(map(int,input().split()))

l1 = list(mdata.union(ndata))

print(l1.__len__())



# m = int(input())
# mdata = set(map(int,input().split()))
# n = int(input())
# ndata = set(map(int,input().split()))
#
# l1 = list(mdata.intersection(ndata))
#
# print(l1.__len__())


# m = int(input())
# mdata = set(map(int,input().split()))
# n = int(input())
# ndata = set(map(int,input().split()))
#
# l1 = list(mdata.symmetric_difference(ndata))
#
# print(l1.__len__())