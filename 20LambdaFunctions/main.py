# Lambda Function or anynomus function this are for convience ------(ONE LINER FUNCTIONS)

def add(x, y, z): return x+y+z
def minus(x, y): return x-y


print(minus(10, 5))
print(add(10, 5, 50))


def a_first(a):
    return a[1]


a = [[1, 4, 2], [50, 2], [8, 1]]
a.sort(key=a_first)  # sorting on base of index 1.
print(a)
