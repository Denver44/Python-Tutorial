# -------------- FILE HANDLING (open and read)---------------------
# To open a file it take two args first is [loaction] & second is [mode].


#------------------------ Reading the file in text Mode which is default.--------------------------------

f = open("2.txt", 'rt')  # f  returns a file pointer.
# content = f.read() # this read function read whole file also we can give the number of words toread.
# print(content)
# content = f.read(7) # this read upto mentioned characters Only.


#-------------------------- Reading the file in Binary Mode.------------------------------------

# f = open("2.txt", 'rb')  # with escape sequences
# content = f.read() # It will read all the line with escape sequence also.
# print(content)

# ------------------------------ READING FILE USING FOR LOOP-------------------------------
# for a in f:
#   if len(a) <= 10:
#     print(a, end="")

# ----------------- readline() function --------------------
content = f.readline() #This read line by line
print(content) #It will read all lines with escape seqeunces

#------------------- readlines() function --------------------
print(f.readlines()) #It will read all lines with escape seqeunces and print a list

f.close() #Closing a file is most important step in file handling.
