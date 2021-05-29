def split_and_join(l):
    l = l.split(" ")
    print(l)
    print(type(l))
    l = "-".join(l)
    print(type(l))
    return l

line = input()
result = split_and_join(line)
print(result)

# here the split function give you list.
# here the jpin function wll return a str.
