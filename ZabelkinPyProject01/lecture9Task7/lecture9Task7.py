class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def displayInfo(self):
         return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.book = []

    def addBook(self, book):
        self.book.append(book)

    def displayAllBooks(self):
        print("Library contents: ")
        for i, book in enumerate(self.book, 1):
            print(f"{i}. {book.displayInfo()}")

    def countBooks(self):
        print(len(self.book))
        


book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
library = Library()

library.addBook(book1)
library.addBook(book2)

library.displayAllBooks()
print("Total books:")
library.countBooks()