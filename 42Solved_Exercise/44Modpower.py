import  math
a = int(input())
b = int(input())
m = int(input())

res = math.pow(a,b)
print(int(res))
res2 = divmod(res,m)
print(int(res2[1]))
