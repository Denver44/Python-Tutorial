# ---------- PYTHoN COMPREHENSION ------------
ls = []
for i in range(100):
    if i%3==0:
        ls.append(i)
    
print(ls)



# -------list comprehension---------------

ls = [i for i in range(100) if i % 5 == 0] 
print(ls)


multiplication = [i*6 for i in range(11)]
print(multiplication)


