test = int(input())
for i in range(test):
    input()
    s1 = set(map(int,input().split()))
    input()
    s2 = set(map(int,input().split()))
    if s1.issubset(s2):
        print(True)
    else:
        print(False)
