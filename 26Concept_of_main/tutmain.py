

def printname(n):
    print(f"Your name is {n}")


def add(a, b):
    print(f"the sum of a + b = {a + b}")


# here the __name__ is our main function.
print("and the name is", __name__)
if __name__ == '__main__':
    printname("durgesh")
    add(56, 55)


# if we run the program here the name will be main and if we import this in another file and if we run there then name will be filename.
