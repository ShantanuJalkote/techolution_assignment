import unittest
from models import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.book_manager.books = []
        self.library.user_manager.users = []
        self.library.checkouts = []

    def test_add_book(self):
        self.library.book_manager.add_book("Test Book", "Test Author", "123456")
        self.assertEqual(len(self.library.book_manager.books), 1)
        self.assertEqual(self.library.book_manager.books[0].get_title(), "Test Book")

    def test_add_user(self):
        self.library.user_manager.add_user("Test User", "1")
        self.assertEqual(len(self.library.user_manager.users), 1)
        self.assertEqual(self.library.user_manager.users[0].get_name(), "Test User")

    def test_checkout_book(self):
        self.library.book_manager.add_book("Test Book", "Test Author", "123456")
        self.library.user_manager.add_user("Test User", "1")
        result = self.library.checkout_book("1", "123456")
        self.assertEqual(result, "Book 123456 checked out to user 1.")
        self.assertFalse(self.library.book_manager.books[0].is_available())

    def test_checkin_book(self):
        self.library.book_manager.add_book("Test Book", "Test Author", "123456")
        self.library.user_manager.add_user("Test User", "1")
        self.library.checkout_book("1", "123456")
        result = self.library.checkin_book("123456")
        self.assertEqual(result, "Book 123456 checked in.")
        self.assertTrue(self.library.book_manager.books[0].is_available())

    def test_add_duplicate_book(self):
        self.library.book_manager.add_book("Test Book", "Test Author", "123456")
        self.library.book_manager.add_book("Test Book", "Test Author", "123456")
        self.assertEqual(len(self.library.book_manager.books), 1)

    def test_checkout_nonexistent_book(self):
        self.library.user_manager.add_user("Test User", "1")
        result = self.library.checkout_book("1", "123456")
        self.assertEqual(result, "User or book not found.")

    def test_checkout_already_checked_out_book(self):
        self.library.book_manager.add_book("Test Book", "Test Author", "123456")
        self.library.user_manager.add_user("Test User1", "1")
        self.library.user_manager.add_user("Test User2", "2")
        self.library.checkout_book("1", "123456")
        result = self.library.checkout_book("2", "123456")
        self.assertEqual(result, "Book is not available.")

    def test_checkin_nonexistent_book(self):
        result = self.library.checkin_book("123456")
        self.assertEqual(result, "Book not found in checkouts.")

if __name__ == "__main__":
    unittest.main()