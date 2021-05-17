

# ---------- DICT  Comphresion ---------------

dict = {i: f"item{i}" for i in range(1, 15) if i %2 == 0}
dict2 = {key: value for key, value in dict.items()}
print(dict)
print(dict2)
