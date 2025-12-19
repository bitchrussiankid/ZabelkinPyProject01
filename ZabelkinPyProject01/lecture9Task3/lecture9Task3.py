# create class:
class Book:
    # class constructor:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # class method:
    def displayInfo(self):
        return f"{self.title} by {self.author}"


book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

print(book1.displayInfo())
print(book2.displayInfo())