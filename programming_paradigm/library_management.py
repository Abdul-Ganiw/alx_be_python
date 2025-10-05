class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def __str__(self):
        status = "Checked out" if self.is_checked_out else "Available"
        return f"{self.title} by {self.author} - {status}"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_available_books(self):
        for book in self.books:
            if not book.is_checked_out:
                print(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                book.is_checked_out = True
                print(f"You have checked out '{book.title}'.")
                return
        print(f"Sorry, '{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_checked_out:
                book.is_checked_out = False
                print(f"You have returned '{book.title}'.")
                return
        print(f"'{title}' was not checked out.")