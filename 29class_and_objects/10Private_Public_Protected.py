# ---------------------------------------------Public - Protected -  Private ---------------------------------------------------------------
# to write variables in protected use ONE underscore and then write variablename  (_protected)
# to write variables in private use TWO underscore and then write variablename  (__private)

class Employee:
    no_of_leaves = 8
    var = 8
    _protectedData = 9
    __privateData = 98

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        print(
            f"The Name is {self.name}. Salary is {self.salary} and role is {self.role} ")


emp = Employee("harry", 343, "Programmer")
emp.printdetails()

print(emp.var)  # directly we can use as it is public


# For Protected Data only this way we can print the private variables . (_classname__privatevariablename)
print(emp._protectedData)
# only this way we can print the private variables . (_classname__privatevariablename)
print(Employee._protectedData)
# NOTE :  only the class inherit from this can use this variable no other class

# For Private Data only this way we can print the private variables . (_classname__privatevariablename)
print(emp._Employee__privateData)

# Check this u will get error.
# print(Employee.__privateData)
# print(emp.__privateData)
