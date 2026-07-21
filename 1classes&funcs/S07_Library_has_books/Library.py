from Book import Book
class Library:
    def __init__(self):
        self.book = Book()
    def borrow_book(self):
        self.book.read()
    