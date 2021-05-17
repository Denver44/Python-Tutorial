
# -------------- ANOTHER METHOD TO OPEN FILE FOR READING --------------------

with open("3.txt") as f:
    a = f.read()
    print(a)
    f.seek(0)
    a = f.read()
    print(a)


# In this we don't have to close file manually it is all handle by the with Only.
