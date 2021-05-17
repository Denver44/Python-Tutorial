# ------------------------------------ Random to generate random number------------------------------------
import random

# -----------------------------here it will give random number from 0 to 10 both inclusive---------------------------
randomnumber = random.randint(0, 10)
print(randomnumber)

# -------------------------------- genearte number betwwn 0 -  100 --------------------------------
rand = random.random() * 100
print(rand)


# ------------------------------------ it pick random item form the list ------------------------------------------
list = ["C", "C++", "Python", "Js", "Ts"]

choice = random.choice(list)
print(choice)
