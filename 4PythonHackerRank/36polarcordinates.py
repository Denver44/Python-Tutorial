import cmath

c = complex(input().strip())
res = cmath.polar(c)
for i in res:
    print('%.3f'%i)
