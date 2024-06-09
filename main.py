# # This is a deliberately poorly implemented main script for a Library Management System.

# import book_management
# import user_management
# import checkout_management

# def main_menu():
#     print("\nLibrary Management System")
#     print("1. Add Book")
#     print("2. List Books")
#     print("3. Add User")
#     print("4. Checkout Book")
#     print("5. Exit")
#     choice = input("Enter choice: ")
#     return choice

# def main():
#     while True:
#         choice = main_menu()
#         if choice == '1':
#             title = input("Enter title: ")
#             author = input("Enter author: ")
#             isbn = input("Enter ISBN: ")
#             book_management.add_book(title, author, isbn)
#             print("Book added.")
#         elif choice == '2':
#             book_management.list_books()
#         elif choice == '3':
#             name = input("Enter user name: ")
#             user_id = input("Enter user ID: ")
#             user_management.add_user(name, user_id)
#             print("User added.")
#         elif choice == '4':
#             user_id = input("Enter user ID: ")
#             isbn = input("Enter ISBN of the book to checkout: ")
#             checkout_management.checkout_book(user_id, isbn)
#             print("Book checked out.")
#         elif choice == '5':
#             print("Exiting.")
#             break
#         else:
#             print("Invalid choice, please try again.")

# if __name__ == "__main__":
#     main()


import logging
from models import Library

main_logger = logging.getLogger('main')
main_logger.setLevel(logging.INFO)
main_handler = logging.FileHandler('./logs/main.log')
main_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
main_handler.setFormatter(formatter)
main_logger.addHandler(main_handler)

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. List Users")
    print("5. Checkout Book")
    print("6. Checkin Book")
    print("7. Track Availability of Book")
    print("8. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    main_logger.info("Starting Library Management System")
    library = Library()
    while True:
        choice = main_menu()
        main_logger.info(f"User choice: {choice}")
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            library.book_manager.add_book(title, author, isbn)
            main_logger.info(f"Book added: {title}, {author}, {isbn}")
        elif choice == '2':
            library.book_manager.list_books()
            main_logger.info("Listing books")
        elif choice == '3':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            library.user_manager.add_user(name, user_id)
            main_logger.info(f"User added: {name}, {user_id}")
            print("\nUser added.")
        elif choice == '4':
            library.user_manager.list_users()
            main_logger.info("Listing users")
        elif choice == '5':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            main_logger.info(f"Checking out book with ISBN {isbn} for user with ID {user_id}")
            print(library.checkout_book(user_id, isbn))
        elif choice == '6':
            isbn = input("Enter ISBN of the book to checkin: ")
            main_logger.info(f"Checking in book with ISBN {isbn}")
            print(library.checkin_book(isbn))
        elif choice == '7':
            isbn = input("Enter ISBN of the book to check availability: ")
            main_logger.info(f"Checking availability of book with ISBN {isbn}")
            book = library.book_manager.search_books(isbn=isbn)
            print(book)
            if book:
                main_logger.info(f"Book {isbn} is {'available' if book[0].is_available() else 'not available'}")
                print(f"Book {isbn} is {'available' if book[0].is_available() else 'not available'}.")
            else:
                main_logger.warning("Book not found")
                print("Book not found.")
        elif choice == '8':
            main_logger.info("Exiting Library Management System")
            print("\nExiting.")
            break
        else:
            main_logger.warning("Invalid choice entered")
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()