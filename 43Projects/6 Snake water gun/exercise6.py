import random

def randomnum():
    n = random.choice([1,2,3])
    return n


playerscore = 0
computerscore = 0

snake = 1
water = 2
gun = 3
computer = randomnum()
i = 0
while i < 3:
    print("Welcome to Snake Water and Gun Game" )
    print("1. Snake")
    print("2. Water")
    print("3. Gun")
    player = int(input("Enter your choice.\n"))
    while player >= 0 and player  <= 3:
        if player == snake and computer == snake:
            print("DRAW")
        elif player == water and computer == water:
            print("DRAW")
        elif player == gun and computer == gun:
            print("DRAW")
        elif player == snake and computer == water:
            print("Player Won")
            playerscore += 1
        elif player == water and computer == gun:
            print("Player Won")
            playerscore += 1

        elif player == gun and computer == snake:
            print("Player Won")
            playerscore += 1
        else:
            print("Computer Won")
            computerscore += 1

        i += 1
        break

    print("PlayerScore :-  ",playerscore ,"  : ComputerScore :- ",computerscore)


if playerscore == computerscore:
    print("Draw")
elif playerscore > computerscore:
    print("YOU WON THE GAME")
elif playerscore < computerscore:
    print("COMPUTER WON")