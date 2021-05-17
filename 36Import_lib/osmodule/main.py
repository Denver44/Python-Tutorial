import os

# print(dir(os))
print(os.getcwd()) # current working directory
os.chdir("E://")  # so this way we can change the directory ffrom D to E.
print(os.getcwd())


# f = open("durgesh.txt")
# print(f.read())
print(os.listdir("D://")) # it will give all the names of the floder of that directory
# os.mkdir("Module") # this is used to make  a folder.
# os.mkdirs("Module") # this is used to make  a folder inside a foler.
# os.rename("jarvis.py","Jarvis.py")
print(os.environ.get("Path"))
# print(os.path.join("D:/","/durgesh.txt")) # it is usde to join to path.
# print(os.path.exists("D://durgesh1.txt"))
# print(os.path.isfile("D://durgesh1.txt"))
# print(os.path.isdir("C://Program Files"))
