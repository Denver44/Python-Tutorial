s1 = set(map(int, input().split()))
n = int(input())

flag = False
for i in range(n):
    s2 = set(map(int, input().split()))
    if s2.issubset(s1):
        if len(s2) == len(s1):
            flag = False
            break
        else:
            flag = True
    else:
        flag = False
        break




print(flag)