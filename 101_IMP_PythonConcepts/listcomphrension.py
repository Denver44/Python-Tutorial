computer = ["sam","ram","rom","ssd"]

s = []
for i in computer:
    if i.startswith('s'):
        s.append(i)
print(s)

# /--------- LIST COMPHRENSION ----------
# first what u want to append
# iterration
# condition
storage = [i for i in computer if i.startswith('s')]
print(storage)

print(id(s) , id(storage))


a = [1,2,3]
# b = a  work as alias.
b = [1,2,3]
print(id(b))
print(id(a))

