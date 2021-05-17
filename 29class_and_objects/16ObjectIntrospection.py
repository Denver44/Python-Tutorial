# ---------- Objects Introspection ----------
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property  #
    def email(self):
        if self.fname == None or self.lname == None:
            return "Emial is not set. Please set it"
        return f"{self.fname}.{self.lname}@gmail.com"

   
    @email.setter
    def email(self, strings):
        names = strings.split('@')[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]


    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None



skillf = Employee("skill" ,"f")
print(id(skillf))

# print(dir(skillf))
# or

import inspect
print(inspect.getmembers(skillf))
