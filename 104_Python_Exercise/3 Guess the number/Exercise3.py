# ------------------------------------------------ GUESS THE NUMBER----------------------------------------------------------------------------------
a = 19
current = 9
counter = 0
while (current):
    b = int(input("Enter a Number and check its is matching with our number or not \n"))

    if b > a:
        print("It is greater than actual number try again\n")
        counter = counter + 1
        current = current-1

    if b < a:
        print("It is Less than actual number try again\n")
        counter = counter + 1
        current = current-1

    if b == a:
        print("Congrats u go it.\n")
        counter = counter + 1
        current = 0


print("total guess it takes around ", counter)
