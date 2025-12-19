def indexChecker(bookIndex):
    try:
        bookIndex = int(bookIndex) - 1

        if bookIndex in range(0, len(books)):
            print(books[bookIndex])
        else:
            print(f"Please, enter the book number (from 1 to {len(books)})")

    except ValueError:
        print(f"Please, enter the book number (from 1 to {len(books)})")

    except Exception as e:
        print("Unknown error")

books = [
    "1984",
    "To Kill a Mockingbird", 
    "The Great Gatsby", 
    "Pride and Prejudice", 
    "The Catcher in the Rye"
    ]

bookIndex = input("Enter book number: ")
indexChecker(bookIndex)