# ----------------- Class Method ---------------------
# By using class methid the instances get the power to chnage the class variablename.
# The big advanatge of cls methid we can use them as consructor.
class car:
    showroomname = "kiya motors"

    def __init__(self, brandname, price, model):
        self.carname = brandname
        self.carprice = price
        self.carmodel = model

    def printcar(self, name):
        print(
            f"{name} your car name is {self.carname} its model number is {self.carmodel} and the price is {self.carprice} and pick the car from {car.showroomname} ")

    # we are making class method here so that the object/instances can also change the class variable .
    @classmethod # here cls is class as here we are dealing will the class so that we have to use cls not self.
    def change(cls, newshowroom):
        cls.showroomname = newshowroom


durgesh = car("BMW", "1.5cr", "M4")
joy = car("Audi", "3.5cr", "Q5")
print(car.showroomname)
durgesh.change("Gayatri Motors") # so here using class method we made our instances capable now that it can change the class variable.It will not chnage only for instance variable, but it will chnage the value for class variable.
durgesh.printcar("DURGESH")
joy.printcar("JOY")
print(car.showroomname)
