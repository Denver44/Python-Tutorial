group = int(input())
list1 = list(map(int, input().split()))

a = set()
b = set()

# first in both element get added if a has the alaready elemnt then it will go in else and it will discard the elment from b as b also added that element it with a.
for people in list1:
    if people not in a:
        a.add(people)
        b.add(people)
    else:
        b.discard(people)

for i in b:
    print(i)