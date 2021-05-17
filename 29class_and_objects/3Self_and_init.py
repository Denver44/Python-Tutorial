# -------------------- Concept os self and __init__() ------------------------
# here the init is called the constructor and self is manadatory.the self act as object here .

class car:
    count = 0  # class variable

    def __init__(self, brandname, price, model):
        self.carname = brandname
        self.carprice = price
        self.carmodel = model
        car.count += 1  # to use class variable use   classname.class_variable_name

    def printdetails(self, name):
        print(f"{name} your car name is {self.carname} its model number is {self.carmodel} and the price is {self.carprice} ")


durgesh = car("BMW", "1.5cr", "M4")
joy = car("Audi", "3.5cr", "Q5")
jay = car("RR", 40, "R1")
durgesh.printdetails("Mr.Durgesh rai")
joy.printdetails("Mr.Joy Christian")
jay.printdetails("Jay")
print(car.count)

# Here when we call joy.printdeatils at that time joy is passed as arg thats why we write self in prindetail function.
