# create class:
class Book:
    # class constructor:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

print(f"book1: {book1.title} by {book1.author}")
print(f"book2: {book2.title} by {book2.author}")