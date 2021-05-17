# ---------------------- Static Method In Python --------------------------
# so both the instances and class directly access this function

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
        return cls(*string.split("-"))

    # ------- STATIC METHOD -------------
    @staticmethod  # static class it dont take slef or class.
    def printname(string):
        print(f"{string} thanks for buying new car")


jay = car
# u can use both class and instnaces to access the static method
jay.printname("Jay Rajput")
car.printname("Jay ")
