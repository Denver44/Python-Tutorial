from itertools import combinations

# print(list(combinations('12345',2)))

sk = list(input().split())

s = sk[0]
k = int(sk[1])
for i in range(1,k+1):
    a = list(combinations(sorted(s),i))
    for j in a:
        for n in j:
            print(n,end="")
        print()



# print(a)