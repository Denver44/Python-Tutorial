# -----------------------------------------------MULTIPLE INHERITANCE-------------------------------------------------
class car:
    var = 10

    def __init__(self, Brand, price, model):
        self.carname = Brand
        self.carprice = price
        self.carmodel = model

    def printcar(self, name):
        print(f"{name} your car name is {self.carname} its model number is {self.carmodel} and the price is {self.carprice}")


class Buyer():
    var = 9

    def __init__(self, name, mob, address, city):
        self.name1 = name
        self.mob = mob
        self.address = address
        self.city = city

    def printcar(self):
        return f"The Buyer name is {self.name1} his personal number is  {self.mob} and his address {self.address} and city name is {self.city} "


# ------------------------------------- MULTIPLE-------------------------------------------------
# by class car and buyer.
# as here car class is writeen first so if we dont make the constructor of the customer class .

class customer(car, Buyer):
    var = 8

    def printdetail(self):
        print(
            f"Your car name is {self.carname} its model number is {self.carmodel} and the price is {self.carprice}")


# here car is written first so as customer car dont have its own constructor so it will run car class customer first.
jay = customer("BMW", "30 lac", "Q3")
jay.printdetail()
print(jay.var)
