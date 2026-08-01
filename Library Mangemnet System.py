class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | {status}"


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"Patron: {self.name} | ID: {self.patron_id}"


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def register_patron(self, patron):
        self.patrons.append(patron)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_patron(self, patron_id):
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                return patron
        return None

    def borrow_book(self, patron_id, isbn):
        patron = self.find_patron(patron_id)
        book = self.find_book(isbn)

        if patron and book:
            if book.borrow():
                patron.borrow_book(book)
                print(f"{patron.name} borrowed '{book.title}'")
            else:
                print("Book is already borrowed.")
        else:
            print("Invalid patron or book.")

    def return_book(self, patron_id, isbn):
        patron = self.find_patron(patron_id)
        book = self.find_book(isbn)

        if patron and book:
            if book in patron.borrowed_books:
                patron.return_book(book)
                book.return_book()
                print(f"{patron.name} returned '{book.title}'")
            else:
                print("This patron has not borrowed the book.")
        else:
            print("Invalid patron or book.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            print(book)

    def display_patrons(self):
        print("\nPatrons:")
        for patron in self.patrons:
            print(patron)
            if patron.borrowed_books:
                print("Borrowed Books:")
                for book in patron.borrowed_books:
                    print("-", book.title)
            else:
                print("Borrowed Books: None")


library = Library()

book1 = Book("Python Programming", "Guido van Rossum", "101")
book2 = Book("Data Structures", "Mark Allen", "102")
book3 = Book("Machine Learning", "Andrew Ng", "103")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

patron1 = Patron("Alice", "P001")
patron2 = Patron("Bob", "P002")

library.register_patron(patron1)
library.register_patron(patron2)

library.display_books()
library.display_patrons()

print("\nBorrowing Books")
library.borrow_book("P001", "101")
library.borrow_book("P002", "103")

library.display_books()
library.display_patrons()

print("\nReturning Book")
library.return_book("P001", "101")

library.display_books()
library.display_patrons()