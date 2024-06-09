import logging
from book import Book
from user import User
from storage import Storage

library_logger = logging.getLogger('library')
library_logger.setLevel(logging.INFO)
library_handler = logging.FileHandler('./logs/library.log')
library_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
library_handler.setFormatter(formatter)
library_logger.addHandler(library_handler)

class Library:
    def __init__(self):
        self.book_manager = BookManager()
        self.user_manager = UserManager()
        self.checkouts = None

    def load_data(self):
        if self.checkouts is None:
            self.checkouts = Storage.load_checkouts()

    def save_data(self):
        self.book_manager.save_books()
        self.user_manager.save_users()
        Storage.save_checkouts(self.checkouts)

    def checkout_book(self, user_id, isbn):
        self.load_data()
        user = self.user_manager.search_users(user_id=user_id)
        book = self.book_manager.search_books(isbn=isbn)
        if len(user) > 0 and len(book) > 0:
            if book[0].is_available():
                self.checkouts.append({"user_id": user_id, "isbn": isbn})
                book[0].set_available(False)
                self.save_data()
                library_logger.info(f"Book {isbn} checked out to user {user_id}.")
                return f"Book {isbn} checked out to user {user_id}."
            else:
                library_logger.warning(f"Book {isbn} is not available.")
                return "Book is not available."
        else:
            library_logger.warning("User or book not found.")
            return "User or book not found."

    def checkin_book(self, isbn):
        self.load_data()
        for checkout in self.checkouts:
            if checkout["isbn"] == isbn:
                self.checkouts.remove(checkout)
                self.book_manager.set_availability(isbn, True)
                self.save_data()
                library_logger.info(f"Book {isbn} checked in.")
                return f"Book {isbn} checked in."
        library_logger.warning("Book not found in checkouts.")
        return "Book not found in checkouts."

class BookManager:
    def __init__(self):
        self.books = None
    
    def load_books(self):
        if self.books is None:
            self.books = Storage.load_books()

    def save_books(self):
        Storage.save_books(self.books)

    def add_book(self, title, author, isbn):
        self.load_books()
        if not any(book.get_isbn() == isbn for book in self.books):
            book = Book(title, author, isbn)
            self.books.append(book)
            self.save_books()
            library_logger.info(f"Added book: {book}")
            print(f"\nAdded book: {book}")
        else:
            library_logger.warning(f"Book with ISBN {isbn} already exists.")
            print(f"\nBook with ISBN {isbn} already exists.")

    def list_books(self):
        self.load_books()
        library_logger.info("Listing books")
        print("\n")
        for book in self.books:
            print(book)

    def search_books(self, isbn):
        self.load_books()
        library_logger.info(f"Searching for book with ISBN {isbn}")
        return [book for book in self.books if book.get_isbn() == isbn]

    def set_availability(self, isbn, availability):
        self.load_books()
        for book in self.books:
            if book.get_isbn() == isbn:
                book.set_available(availability)
                library_logger.info(f"Book {isbn} availability set to {availability}")
                self.save_books()
                break

class UserManager:
    def __init__(self):
        self.users = None

    def load_users(self):
        if self.users is None:
            loaded_users = Storage.load_users()
            self.users = loaded_users if loaded_users is not None else []

    def save_users(self):
        Storage.save_users(self.users)

    def add_user(self, name, user_id):
        self.load_users()

        while any(user.get_user_id() == user_id for user in self.users):
            print(f"User ID '{user_id}' already exists.")
            user_id = input("Please enter a new user ID: ")

        user = User(name, user_id)
        self.users.append(user)
        library_logger.info(f"Added user: {user}")
        self.save_users()
        
    def list_users(self):
        self.load_users()
        library_logger.info("Listing users")
        print("\n")
        for user in self.users:
            print(user)

    def search_users(self, user_id):
        self.load_users()
        library_logger.info(f"Searching for user with ID {user_id}")
        return [user for user in self.users if user.get_user_id() == user_id]
