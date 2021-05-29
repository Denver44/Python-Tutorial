# The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

from collections import defaultdict

d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print(i)

word = "AAAABBBBAAAAAA"
dict = {}
for c in word:
    if c not in dict:
        dict[c] = 1
    else:
        dict[c] += 1

print(dict)

# # ------------ SIMPLEST WAY BY USING DEFAULT DICT ----------------

d = defaultdict(int)
for c in word:
    d[c] += 1

for i in dict.items():
    print(i)