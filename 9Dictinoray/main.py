# ------------------------------------------ Dictionary-------------------------------------
#  Dictionary is nothing but key value pairs
d1 = {}
# print(type(d1))
d2 = {"Harry": "Burger",
      "Rohan": "Fish",
      "SkillF": "Roti",
      "Shubham": {"B": "maggie", "L": "roti", "D": "Chicken"}}

# This we can add new key value in our Dict.
d2["Ankit"] = "Junk Food"
d2[420] = "Kebabs"
print(d2)
del d2[420]  # to delete and key value pair use del(key);
print(d2)
print(d2["Shubham"])
# d3 = d2.copy()
# del d3["Harry"]
d2.update({"Leena":"Toffee"})
print(d2.keys())
print(d2.items())
