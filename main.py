from commands.add import add_book, add_user
from database.db import get_connection
from commands.list import list_books, list_users
from commands.borrow_and_return import borrow_book, return_book, current_borrowings
from commands.search import search_book
from commands.delete import delete_book, delete_user

connection = None

try:
    connection = get_connection()
    while True:
        print("1. Add user")
        print("2. Add book")
        print("3. List users")
        print("4. List books")
        print("5. Search books")
        print("6. Borrow book")
        print("7. Return book")
        print("8. Show current borrowings")
        print("9. Delete user")
        print("10. Delete book")
        print("0. Exit")
        
        choice = input("Choose one of these options: ")
        
        if choice == "1":
            add_user(connection)
        elif choice == "2":
            add_book(connection)
        elif choice == "3":
            list_users(connection)
        elif choice == "4":
            list_books(connection)
        elif choice == "5":
            search_book(connection)
        elif choice == "6":
            borrow_book(connection)
        elif choice == "7":
            return_book(connection)
        elif choice == "8":
            current_borrowings(connection)
        elif choice == "9":
            delete_user(connection)
        elif choice == "10":
            delete_book(connection)
        elif choice == "0":
            break
        else:
            print("Invalid input.")
finally:
    if connection is not None:
        connection.close()