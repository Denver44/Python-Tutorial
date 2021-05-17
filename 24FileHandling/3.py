# ----------------------- FILE IN WRITING MODE -----------------------------------
# In writing mode if there is no file exist then it will create a new file of the name.


# f = open("3.txt", "w")
# user = input()
# a = f.write(user) # the write function returns the number of line its written in the file.
# print(a) # It will display the toatl line written


# --------------------- FILE IN APPEND MODE -----------------------------
# It actually write the content at the end fo file
# f = open("3.txt", "a")
# a = f.write(" Hey durgesh your new file is created")

# ------------ FILE in r+ mode we can both read and write -------------------------
f = open("3.txt", "r+")
content = f.read()
print(content)

f.write("\tRead and Write mode")

f.seek(0) # using seek function we set the file ptr again to start.

content = f.read()
print(content)

f.close() #Closing a file is most important step in file handling.
