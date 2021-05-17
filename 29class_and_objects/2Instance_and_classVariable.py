class Employee:
    # this class variable so it will be avialble for every object of the calss.
    lunch_time = "12:30PM"
    pass


durgesh = Employee()
joy = Employee()

durgesh.name = "Durgesh Rai"
joy.name = "Joy Christian"
durgesh.job = "web designer"
joy.job = "test engineer"

print(durgesh.name, end=" ")
print(durgesh.job)
print(joy.name, end=" ")
print(joy.job)
Employee.lunch_time = "01:00PM"
# only employe class can chnage the data of the template class, instnace(objects) cannot chnage the data of the class template.
print("Lunch time of Joy ", joy.lunch_time)
print("Lunch time of durgesh ", durgesh.lunch_time)
joy.lunch_time = "02:00PM"
# It will create a new variable for joy lunch_time and set the value, it cannot chnage the class variable lunch_time value.
print(joy.__dict__)
print(durgesh.__dict__)
print("Lunch time of Joy ", joy.lunch_time)
print("Lunch time of Joy ", durgesh.lunch_time)
