# ------------------------------ SUPPER().__init()__----------------------------

# super().__init__() this helps us to call the super class constructor.

class A:
    classvar1 = "I am in class A"

    def __init__(self):
        self.var1 = "I am var1  inside a class A's Constructor"
        self.classvar1 = "Instances var in class A"
        self.special = "Special"


class B(A):
    classvar2 = "I am in class B......"

    def __init__(self):
        # if it is written below then classvar1 of A will be printed if we call classvar1.
        super().__init__()
        # if we dont write this it will no take the  constructor of the class A here so the constructor function will not be executed.
        self.var2 = "I am var1  inside a class B's Constructor"
        self.classvar1 = "Instances var in class B"


a = A()
b = B()
print(b.classvar1)
print(b.var1)
print(b.special)
print(b.classvar2)
print(b.var2)
print(b.classvar1)

# First it will check that any variable is in constructor or not of name classvar1 then it will check in the class.
