xk = list(map(int,input().split()))
x = xk[0]
k = xk[1]
b = input()
res = eval(b)
if  res == k:
    print(True)
else:
    print(False)
