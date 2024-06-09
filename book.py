class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_isbn(self):
        return self.isbn

    def is_available(self):
        return self.available

    def set_available(self, value):
        self.available = value

    def __repr__(self):
        return f"Book(title={self.get_title()}, author={self.get_author()}, isbn={self.get_isbn()}, available={self.is_available()})"
