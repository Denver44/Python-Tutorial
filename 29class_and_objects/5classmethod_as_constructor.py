class car:
    showroomname = "kiya motors"

    def __init__(self, brandname, price, model):
        self.carname = brandname
        self.carprice = price
        self.carmodel = model

    def printcar(self, name):
        print(
            f"{name} your car name is {self.carname} its model number is {self.carmodel} and the price is {self.carprice} ")

    @classmethod
    def change(cls, newshowroom):
        cls.showroomname = newshowroom

    @classmethod  # clas method as constructor.
    def from_dash(cls, string):
        return cls(*string.split("-"))  # here the cls is class car


joy = car("BMW", "25 lac", "Q3")

jay = car.from_dash("Mercedes-5.5cr-A6")
# this work as alternative constructor

jay.printcar("Jay")
joy.printcar("Joy")
