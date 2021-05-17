# ---------------------- SOme usefull file functions -------------------------------
f = open("3.txt")
print(f.tell())  # this tell the location of the file pointer in the text file.
print(f.readline())
print(f.tell())
print(f.readline())
f.seek(7)  # using fseek we can put the file pointer where we want.
print(f.readline())
f.close()
