class Bookshelf:
    def __init__(self,*books):
        self.books = books

    def __str__(self):
        return f"Bookshelf has {len(self.books) } {type(self.books)}"


class Book:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return  f"The book name is {self.name}"



b1 = Book("C++")
b2 = Book("Python")
b3 = Book("C")
print(b1)
print(b2)
shelf = Bookshelf(b1,b2,b3)
print(shelf)
