# ---------- setters and property decorators ----------


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property  # Propert decorators now it is a proprety not a function.
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it"
        else:
            return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter  # creating a setter using a decorator.
    def email(self, strings):
        names = strings.split('@')[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


a = Employee("Raj", "Patel")
b = Employee("Jay", "Rajput")

print(a.explain())
print(a.email)

a.fname = "Jay"

print(a.explain())
print(a.email)
a.email = "this.that@gmail.com"
print("After setter")
print(a.email)
print(a.explain())

print("After deleter")
del a.email
print(a.email)
print(a.fname)
print(a.lname)
a.email = "this.that@gmail.com"
print(a.email)
