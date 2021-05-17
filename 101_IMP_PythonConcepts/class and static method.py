class Bookstore:
    Types = ("Hardcover", "paperback")

    def __init__(self, name, type, weight):
        self.name = name
        self.type = type
        self.weight = weight

    @classmethod
    def harcover(cls, name, weight):
        return f"the name of the book {name} and it is {cls.Types[0]} and its weight is {weight}"

    @classmethod
    def paperback(cls, name, weight):
        return f"the name of the book {name} and it is {cls.Types[1]} and its weight is {weight}"

    @staticmethod
    def thank():
        print("Thanks for shopping")


b = Bookstore.harcover("python", 101)
print(b)
Bookstore.thank()
