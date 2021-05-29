if __name__ == '__main__':
    N = int(input())

    list1 = []
    for i in range(N):
        task = input().split()
        if (task[0] == 'insert'):
            list1.insert(int(task[1]), int(task[2]))
        elif (task[0] == 'print'):
            print(list1)
        elif (task[0] == "remove"):
            list1.remove(int(task[1]))
        elif (task[0] == "append"):
            list1.append(int(task[1]))
        elif (task[0] == "sort"):
            list1.sort()
        elif (task[0] == "reverse"):
            list1.reverse()
        elif (task[0] == "pop"):
            list1.pop()

# a = input().split()
# print(a)
