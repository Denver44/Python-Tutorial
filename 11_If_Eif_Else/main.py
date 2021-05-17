# ----------------- IF elif and else----------------------------------
var1, var2 = 6, 56
var3 = int(input())
if var3 > var2:
    print("Greater")
elif var3 == var2:
    print("Equal")
else:
    print("Lesser")

# -----------------------------  in vs not in -------------------------------


list1 = [5, 7, 3]
print(15 in list1)  # return boolean value.


if 5 not in list1:
    print("No its not in the list")
else:
    print("its there")

# ---------------------------- Short hand if and else-------------------------------
a = int(input())
b = int(input())
print("A is greater then B") if(a > b) else print("B is greater than A")
