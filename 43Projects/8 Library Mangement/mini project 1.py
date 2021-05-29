import datetime
class Libaray:
    i = 0

    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lenddict = {}
        Libaray.i = 0

    def displaybook(self):
        with open("Libbook.txt", "a") as f:
            print(f"The Books in {self.name} Libarary are:- ")
            for book in self.booklist:
                Libaray.i += 1
                f.write(f"{Libaray.i}  {book}\n")
                print(Libaray.i, " ", book)
        print("\n")

    def lendBook(self, user, book):

        if book not in self.lenddict.keys():
            self.lenddict.update({book: user})
            print("Datatabase Updated\n")
            with open("Libbooklend.txt", "a") as f:
                f.write(f"On {datetime.datetime.now()}  {user} Lended  {book}\n")

        else:
            print(f"Book is already leneded by {self.lenddict[book]}")


    def addBook(self, book):
        with open("Libbook.txt", "a") as f:
            Libaray.i += 1
            f.write(f"{Libaray.i}  {book}\n")
        self.booklist.append(book)
        print("Book Sucessfully added\n")


    def returnbook(self, book, user):
        with open("Libbookreturn.txt", "a") as f:
            f.write(f"{book} is returned on {datetime.datetime.now()} by {user}\n")
        self.lenddict.pop(book)
        print("\n")


if __name__ == '__main__':
    books = ["Python", "Javascript", "Django", "flask", "C", "C++", "HTML", "CSS", "DSA"]
    LibName = "Peterson"
    peterson = Libaray(books, LibName)

    choice = 1
    while choice != 0:
        print(f"Welcome to {LibName} Library")
        print("1. For dipslay book")
        print("2. For Lending book")
        print("3. For Donating book")
        print("4. For Returning book")
        print("0. quit\n")
        choice = int(input())

        if choice == 1:
            peterson.displaybook()
        elif choice == 2:
            print("Enter Your name and Book which u want to Borrow ")
            user = input()
            book_borrow = input()
            peterson.lendBook(user, book_borrow)

        elif choice == 3:
            print("Enter name Book which u want to Donate ")
            book_donate = input()
            peterson.addBook(book_donate)

        elif choice == 4:
            print("Enter name Book which u want to Return ")
            book_return = input()
            user_name = input()
            peterson.returnbook(book_return, user_name)

        elif choice == 0:
            break
