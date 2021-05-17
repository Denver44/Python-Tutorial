# ------------ Operator Overloadimng ------------------
class Employee:

    def __init__(self, name, age, salaray):
        self.name = name
        self.age = age
        self.salaray = salaray

    def print(self):
        return f"{self.name} his age is {self.age} and his slaary is {self.salaray} "

    # This is special method and we call it dunder method it actuallys help to overload the operator.
    def __add__(self, other):
        return (self.age) + (other.age), (self.salaray) + (other.salaray)

    def __repr__(self):
        return f"Employee '{self.name}' {self.age} {self.salaray}"

# To define a object we use Str method
    def __str__(self):
        return f"{self.name} his age is {self.age} and his slaary is {self.salaray} "


e1 = Employee("Durgesh rai", 21, 100)
e2 = Employee("Joy Christian", 22, 500)
print(e1.print())
print(e1.__add__(e2))
print(e1.__str__())
print(e1.__repr__())
print(e1)  # it will always print str if its there else it will print repr

# dunder methods which are start and end by underscore(_).
