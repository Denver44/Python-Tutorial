from collections import deque
n = int(input())
d = deque()

for i in range(n):
    a = list(input().split())

    if a[0] == "append":
        d.append(int(a[1]))
    elif a[0] == "appendleft":
        d.appendleft(int(a[1]))
    elif a[0] == "pop":
        d.pop()
    elif a[0] == "popleft":
        d.popleft()


for a in range(len(d)):
    print(d[a],end=" ")

