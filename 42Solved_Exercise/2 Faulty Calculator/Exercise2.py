#----------------------------------------------- FAULTY CALCULATOR-------------------------------------------------------------------#
operator = input("Enter the opeartor ")
a = int(input("Enter the first value "))
b = int(input("Enter the second value "))

if operator == '+':
    if a == 45 and b == 3:
        print(int(555))
    else:
        print(int(a + b))

if operator == '-':
    if a == 5679 and b == 77:
        print(int(5200))
    else:
        print(int(a - b))

if operator == '/':
    if a == 56 and b == 6:
        print(int(3))

    else:
        print(int(a / b))
