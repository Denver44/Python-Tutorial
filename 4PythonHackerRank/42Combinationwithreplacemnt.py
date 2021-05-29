from itertools import combinations_with_replacement

sk = input().split()
s = sk[0]
k = int(sk[1])


a = list(combinations_with_replacement(sorted(s),k))

for i in a:
    for n in i:
        print(n,end="")
    print()