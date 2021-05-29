from itertools import permutations
o = (input().split())
a = o[0]
l = list()
k = list()
for i in a:
    l.append(ord(i))

l.sort()

for i in l:
    k.append(chr(i))

w = "".join(k)
w = w.upper()

b = int(o[1])
m = list(permutations(w,b))
p = list(m)

for i in range(len(p)):
    x = p[i]
    print(x)
    for j in range(b):
        print(x[j],end="")
    print()



