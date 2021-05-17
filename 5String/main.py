# ---------------------------------------------- STRING-------------------------------------------
mystr = "aABCDEFGHIJKLMNOPQRSTUVWXYZ"
var1 = "123"
var2 = "14564"

# print(len(mystr)) # To get Lenght of String use => len() Function
# print(mystr[8])
# print(mystr[25])
# print(mystr[3:10]) # last will be excluding [start-Indexing: stop-indexing]
# print(mystr[1:15:3]) # last will be excluding [start-Indexing: stop-indexing: JumpBy] Start alwasy from 2
# print(mystr[::-1]) # ShortHand For reversing a String.
# print(mystr[::-2]) # But first it will reverse the string and then skip the characters by 1.
# print(mystr.find('Z')) # -1 return thats means the charcters is not found in our string else it will give the index of charcter.
# print(mystr.endswith("z"))
# print(mystr.startswith("A"))
# print(mystr.count("A"))
# print(mystr.capitalize())
# print(mystr.lower())
# print(mystr.upper())
# print(mystr.replace("JK", "**"))

# delete the string from left side if it get the Character in the string which u have pass but at least first charcter should be there  .
print(mystr.lstrip('ADBC'))


# delete the string from right side if it get the Character in the string which u have pass. same but last starting char must be there.
print(mystr.rstrip('XY'))


# Returns True if all characters in the string are in the alphabet
print(mystr.isalpha())

# Returns True if all characters in the string are in the alphabet
print(var1.isalpha())

# Returns True if all characters in the string are decimals means (0-9)
print(var2.isdecimal())

# Returns True if all characters in the string are digits
print("hi", var1.isdigit())
print(var2.isdigit())  # Returns True if all characters in the string are digits


# ------------------------ STRING JOIN FUNCTIONS ---------------------------------------------

list = ['Joy', 'Jay', 'Durgesh', 'Rahul']
str = '=>'
# Joins the elements of an iterable to the end of the string
print(str.join(list))


# -------------------------------- IMPORTANT---------------------------
# str = "DURGESH" # str[0] ='v'  #This Operation cannot Be Perfomed int the String
# print(id(str))
# str = "VISHAL"  # Here the New memory Located and Vishal Got store there and then str and have the adddress of the new memory.
# print(id(str))
