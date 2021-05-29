size = int(input())
set1 = set(map(int, input().split()))

n = int(input())

for i in range(n):
    query = input().split()

    if query[0] == 'intersection_update':
        set2 = set(map(int, input().split()))
        set1.intersection_update(set2)

    elif query[0] == 'update':
        set2 = set(map(int, input().split()))
        set1.update(set2)

    elif query[0] == 'symmetric_difference_update':
        set2 = set(map(int, input().split()))
        set1.symmetric_difference_update(set2)

    elif query[0] == 'difference_update':
        set2 = set(map(int, input().split()))
        set1.difference_update(set2)

print(sum(set1))