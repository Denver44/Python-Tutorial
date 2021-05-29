from collections import  OrderedDict
n = int(input())
OrderedDict = {}
b= []
for i in range(n):
    a = input()
    b = a.rpartition(' ')
    if b[0] in OrderedDict:
        OrderedDict[b[0]] += int(b[2])
    else:
        OrderedDict[b[0]] = int(b[2])


for i in OrderedDict.keys():
    print(i,OrderedDict[i])
#
# b= []
# a = "Banana Chips 30"
# b = a.rpartition(' ')
# print(b[0])
# print(b[2])