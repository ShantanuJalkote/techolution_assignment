import json
import logging
from book import Book
from user import User

storage_logger = logging.getLogger('storage')
storage_logger.setLevel(logging.INFO)
storage_handler = logging.FileHandler('./logs/storage.log')
storage_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
storage_handler.setFormatter(formatter)
storage_logger.addHandler(storage_handler)

class Storage:
    @staticmethod
    def load_books():
        storage_logger.info("Loading books from file.")
        return Storage._load_data("./data/books.json", Book)

    @staticmethod
    def save_books(books):
        storage_logger.info("Saving books to file.")
        Storage._save_data("./data/books.json", books)

    @staticmethod
    def load_users():
        storage_logger.info("Loading users from file.")
        return Storage._load_data("./data/users.json", User)

    @staticmethod
    def save_users(users):
        storage_logger.info("Saving users to file.")
        Storage._save_data("./data/users.json", users)

    @staticmethod
    def load_checkouts():
        storage_logger.info("Loading checkouts from file.")
        return Storage._load_data("./data/checkouts.json")

    @staticmethod
    def save_checkouts(checkouts):
        storage_logger.info("Saving checkouts to file.")
        Storage._save_data("./data/checkouts.json", checkouts)

    @staticmethod
    def _load_data(filename, cls=None):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                if cls==Book:
                    return [cls(item["title"], item["author"], item["isbn"]) for item in data]
                elif cls==User:
                    return [cls(item["name"], item["user_id"]) for item in data]
                return data
        except FileNotFoundError:
            storage_logger.warning(f"File '{filename}' not found.")
            return []

    @staticmethod
    def _save_data(filename, data):
        try:
            with open(filename, 'w') as file:
                if isinstance(data, list) and data and isinstance(data[0], (Book, User)):
                    json.dump([item.__dict__ for item in data], file)
                else:
                    json.dump(data, file)
            storage_logger.info(f"Data saved to '{filename}'.")
        except Exception as e:
            storage_logger.error(f"Error occurred while saving data to '{filename}': {e}")
