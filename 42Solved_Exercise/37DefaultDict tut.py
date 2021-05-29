from collections import defaultdict

nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]

l = list()
d = defaultdict(list)
for i in range(1, n + 1):
    d[input()].append(i)

# print(d)
l = []
for j in range(0, m):
    l.append(input())

for k in l:
    if k in d.keys():
        for x in d[k]:
            print(x,end=" ")
        print()
    else:
        print(-1)
