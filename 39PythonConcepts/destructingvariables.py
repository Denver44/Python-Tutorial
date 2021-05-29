x = 5,11
# or
y = (5,11)
print(type(x))
# -- DIFFRENT this 5,11 and [(5,11)] nad [5,11]
a = [5,11]
print(a)

people = [("bob",42,"Mechanic"),("jhon",24,"programmer"),("joe",21,"developer")]

for name,age,profession in people:
    print(name,age,profession)

candid1,candid2,candid3 = people
print(candid1)
print(candid2)
print(candid3)