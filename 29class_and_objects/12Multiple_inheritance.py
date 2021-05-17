# ------------------------- MULTIPLE INHERITANCE---------------------------

class A:
    def met(self):
        print("I am in class A")


class B(A):
    def met(self):
        print("I am in class B")


class C(A):
    def met(self):
        print("I am in class C")


class D(B, C):
    def met(self):
        print("I am in class D")


a = A()
b = B()
c = C()
d = D()
d.met()

# first it will check in d is there in met function if it there then it will do its work.
# else it will go and check on B.
# else if it not found in B then checks it in C.
# If both in b & C it didnt grt then it will go the parent of B class A because b is written first.
