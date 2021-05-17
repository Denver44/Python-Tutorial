# ------ TRY EXCEPT ELSE FINALLY------------------------
f1 = open("17Try_Except_Else_Finally/1.txt")

try:
    content = f1.read()
    f = open("17Try_Except_Else_Finally/2.txt")

except Exception as e:
    print(e)

else:
    print("This will run only if except is not running")


# If we want that this work must be done then we used finally.
finally:
    print("Run this anyway...")
    f.close()
    print(content)
    f1.close()

print("Important stuff")


# We can write more than except.
# Because there are different error :
# EOFERROR
# IOError
