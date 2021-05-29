class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f"The name is {self.name} and his age is {self.age}"

    # at Debigging time we use the repr method
    
    def __repr__(self):
        return f"< {self.name}  {self.age}>"


p1 = person("Durgesh", 21)
print(p1)
