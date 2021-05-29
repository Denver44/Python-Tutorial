#--------------------------------------------------- STAR  PRINTING  UPSIDE/DOWNSIDE------------------------------------------------------------------#
a = int(input("Enter the numbers of rows u want "))
b = int(input("enter 0 or 1 "))
c = bool(b)
if b == True:
    for i in range(0, a):
        for j in range(0, a):
            if i >= j:
                print("*", end=" ")
        print()

if b == False:
    for i in range(0, a):
        for j in range(0, a):
            if i <= j:
                print("*", end=" ")
        print()
