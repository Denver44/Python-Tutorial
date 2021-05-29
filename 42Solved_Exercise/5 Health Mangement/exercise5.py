import datetime


def info2(a):
    print("For " + a + " what u want to save in log book select the option.")
    print("1.Execise plan")
    print("2.Diet chart")
    print("0.Quit")
    plan = int(input())
    return plan


def info(a):
    print("For " + a + "which data u want reterive.")
    print("1.Execise plan")
    print("2.Diet chart")
    plan = int(input())
    return plan


def gettime():
    return datetime.datetime.now()


print("HEALTH   MANGEMENT")
print("1. For Enter Data")
print("2. For Reterive Data")
choice = int(input())

if choice == 1:
    print("Enter the Number for which client u want to save data")
    print("1.Neeraj")
    print("2.Vishal")
    print("3.Harshil")
    num = int(input())

    if num == 1:
        a = "Neeraj"
        condition = True
        while condition:
            plan = info2(a)
            if plan == 1:
                with  open("neerajexe.txt" , "a+") as f:
                    data = gettime()
                    content = input()
                    f.write(str(data) + " " + content + "\n")
            elif plan == 2:
                with open("neerajdiet.txt", "a+") as f:
                    data = gettime()
                    content = input()
                    f.write(str(data) + " " + content + "\n")
            elif plan == 0:
                condition = False


    elif num == 2:
        a = "Vishal"
        condition = True
        while condition:
            plan = info2(a)
            if plan == 1:
                with open("vishalexe.txt", "a+") as f:
                    data = gettime()
                    content = input()
                    f.write(str(data) + " " + content + "\n")
            elif plan == 2:
                with open("vishaldiet.txt", "a+") as f:
                    data = gettime()
                    content = input()
                    f.write(str(data) + " " + content + "\n")
            elif plan == 0:
                condition = False
    else:
        a = "Harshil"
        condition = True
        while condition:
            plan = info2(a)
            if plan == 1:
                with open("harshilexe.txt", "a+") as f:
                    data = gettime()
                    content = input()
                    f.write(str(data) + " " + content + "\n")
            elif plan == 2:
                with open("harshildiet.txt", "a+") as f:
                    data = gettime()
                    content = input()
                    f.write(str(data) + " " + content + "\n")
            elif plan == 0:
                condition = False

else:
    print("Enter the Number for which client u want to reterive data")
    print("1.Neeraj")
    print("2.Vishal")
    print("3.Harshil")
    num = int(input())

    if num == 1:
        a = "Neeraj"
        plan = info(a)

        if plan == 1:
            with  open("neerajexe.txt") as f:
                textprint = f.read()
                print(textprint)

        else:
            with  open("neerajdiet.txt") as f:
                textprint = f.read()
                print(textprint)

    elif num == 2:
        a = "Vishal"
        plan = info(a)

        if plan == 1:
            with  open("vishalexe.txt") as f:
                textprint = f.read()
                print(textprint)

        else:
            with  open("vishaldiet.txt") as f:
                textprint = f.read()
                print(textprint)

    else:
        a = "Harshil"
        plan = info(a)

        if plan == 1:
            with  open("harshilexe.txt") as f:
                textprint = f.read()
                print(textprint)

        else:
            with  open("harshildiet.txt") as f:
                textprint = f.read()
                print(textprint)
