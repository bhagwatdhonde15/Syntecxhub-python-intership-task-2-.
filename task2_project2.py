import json

class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.issued = False

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.id] = book

    def search(self, keyword):
        for b in self.books.values():
            if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower():
                print(b.id, b.title, b.author, "Issued" if b.issued else "Available")

    def issue_book(self, id):
        if id in self.books and not self.books[id].issued:
            self.books[id].issued = True

    def report(self):
        print("Total books:", len(self.books))
        print("Issued books:", sum(b.issued for b in self.books.values()))

# --------- Usage ---------
lib = Library()

lib.add_book(Book(1, "Python Basics", "Guido"))
lib.add_book(Book(2, "Data Structures", "Mark"))

lib.issue_book(1)
lib.search("python")
lib.report()
