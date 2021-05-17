# -------------------------------- CLASS AND OBJECTS----------------------------
# Class  - Template.
# Object - Instance of the Class
class Student:
    pass  # if your not right anything then write pass.


# -- objects are durgesh and joy
durgesh = Student()
joy = Student()

# Variables for our instances.
durgesh.name = "Durgesh Rai"
joy.name = "Joy Christian"
durgesh.sub = ["maths", "physics"]
joy.sub = ["chemstriy", "Env"]

print(durgesh.name, end=" ")
print(durgesh.sub)
print(joy.name, end=" ")
print(joy.sub)
print(type(durgesh))
