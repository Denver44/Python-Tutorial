if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1 = list(arr)


    list1.sort()
    list1.reverse()
    max = list1[0]
    min = 0
    i = 1
    while True:
        if list1[i] == max:
            i+=1
        else:
            min =list1[i]
            break

print(min)
