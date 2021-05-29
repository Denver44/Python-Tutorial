cube = lambda x: x * x * x


def fibonacci(n):
    i = 2
    l = list()
    if n == 1:
        l.append(0)
        return l
    if n == 0:
        return l

    firsttem = 0
    secondterm = 1
    l.append(firsttem)
    l.append(secondterm)
    while i != n:
        newterm = firsttem + secondterm
        l.append(newterm)
        firsttem = secondterm
        secondterm = newterm
        i += 1
    return l


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))