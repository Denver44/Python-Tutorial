if __name__ == '__main__':
    size = int(input())
    student = list()

    for size in range(size):
        name = input()
        score = float(input())
        student.append([score, name])

    student.sort()
    print(student)
    min = student[0][0]
    lowest = 0

    i = 1
    while True:
        if student[i][0] == min:
            i = i + 1
        else:
            lowest = student[i][0]
            j = i
            for j in range( i,len(student)):
                if student[j][0] == lowest:
                    print(student[j][1])
            break

#As here we have to find the second lowest not he first .