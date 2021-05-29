num = int(input())
s = set(map(int, input().split()))

command = int(input())

while command :
    query = input().split()
    if (query[0] == 'pop'):
        s.pop()
    elif (query[0] == 'remove'):
        s.remove(int(query[1]))
    elif (query[0] == 'discard'):
        s.discard(int(query[1]))
    command -= 1

print(sum(s))
