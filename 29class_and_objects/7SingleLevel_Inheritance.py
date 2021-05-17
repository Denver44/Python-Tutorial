#------------------------------single Level inheritance:--------------#
class car:
    showroomname = "kiya motors"

    def __init__(self, Brand, price, model):
        self.carname = Brand
        self.carprice = price
        self.carmodel = model

    def printcar(self, name):
        print(f"{name} your car name is {self.carname} its model number is {self.carmodel} and the price is {self.carprice} purcahsed form {self.showroomname} ")

    @classmethod
    def change(cls, newshowroom):
        cls.showroomname = newshowroom

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def thankYou_msg(string):
        print(f"{string} thanks for buying new car form ")


# ------------- Inheritance------------------------------------


class Buyer(car):  # here the car is inherit .

    # constructor of buyer class.
    def __init__(self,  Brand, price, model, name, mob, address, city):
        self.carname = Brand
        self.carprice = price
        self.carmodel = model
        self.name = name
        self.mob = mob
        self.address = address
        self.city = city
        # In further tutuorial we will learn the concept of super which will help us to run the super class constructor. so we dont have to repeat the code like here we did it.

    def Buyerdetails(self):
        print(
            f"The Buyer name is {self.name}. mobile number : {self.mob} and his address {self.address} , city name is {self.city} and he bought {self.carname} model {self.carmodel} cost {self.carprice}")


# here the car class all method and attributes are now in buyer calss
jay = Buyer("BMW", "30 lac", "Q3", "Jay",
            "+91123456789", "Nizampura", "Vadoadara")
jay.Buyerdetails()
# using Buyer class we acess the car class methods. this is called inheritance
jay.printcar("Mr.Jay Rajput")
jay.thankYou_msg("Jay")
