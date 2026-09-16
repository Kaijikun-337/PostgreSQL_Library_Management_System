def borrow_book(connection):
    
    while True:
        try:
            user_id = int(input("Enter an ID of a user: "))
        except ValueError:
            print("Please enter a valid ID. (e.g. 25)")
        else:
            break
         
    cursor = connection.cursor()
    
    user_search_query = """SELECT * FROM users WHERE user_id = %s""" 
    cursor.execute(user_search_query, (user_id,))    
    user_result = cursor.fetchone()
    
    if not user_result:
        print("User not found")
        cursor.close()
        return

    while True:
        try:
            book_id = int(input("Enter an ID of a book: "))
        except ValueError:
            print("Please enter a valid ID. (e.g. 25)")
        else:
            break
    
    book_search_query = """SELECT * FROM books WHERE book_id = %s"""
    cursor.execute(book_search_query, (book_id,))
    book_result = cursor.fetchone()
    
    if not book_result:
        print("Book not found")
        cursor.close()
        return
    
    borrow_book_check_query = """SELECT borrowed_book_id FROM users WHERE user_id = %s"""
    cursor.execute(borrow_book_check_query, (user_id,))
    borrow_result = cursor.fetchone()
    
    if borrow_result[0] is not None:
        print("User has alredy borrowed a book.")
        cursor.close()
        return

    user_borrowed_book_query = """SELECT borrowed_by_user FROM books WHERE book_id = %s"""    
    cursor.execute(user_borrowed_book_query, (book_id,))
    user_borrow_result = cursor.fetchone()
    
    if user_borrow_result[0] is not None:
        print("Book is alredy borrowed.")
        cursor.close()
        return
    
    update_book = """UPDATE books SET borrowed_by_user = %s WHERE book_id = %s"""
    update_user = """UPDATE users SET borrowed_book_id = %s, borrowed_at = CURRENT_TIMESTAMP, returned_at = NULL WHERE user_id = %s"""
    
    cursor.execute(update_book, (user_id, book_id))
    cursor.execute(update_user, (book_id, user_id))
    
    connection.commit()
    cursor.close()
    
def return_book(connection):
    print("Choose how you want to return a book:")
    print("1. By book ID")
    print("2. By user ID")
    
    choice = input("Choose the option: ")
    
    cursor = connection.cursor()
    
    if choice == "1":
        while True:
            try:
                book_id = int(input("Insert the book id: "))
            except ValueError:
                print("Please enter a valid book id. (e.g. 25)")
            else:
                break
        
        sql_query = """SELECT borrowed_by_user FROM books WHERE book_id = %s"""
        cursor.execute(sql_query, (book_id,))
        result = cursor.fetchone()
        
        if result is None or result[0] is None:
            print("The book is not borrowed")
            cursor.close()
            return
        
        user_id = result[0]
        
        book_return_query = """UPDATE books SET borrowed_by_user = NULL WHERE book_id = %s"""
        user_return_query = """UPDATE users SET borrowed_book_id = NULL, returned_at = CURRENT_TIMESTAMP WHERE user_id = %s"""
        cursor.execute(book_return_query, (book_id,))
        cursor.execute(user_return_query, (user_id,))
        
        connection.commit()
        cursor.close()
        print("Book returned")
        
        
    elif choice == "2":
        while True:
            try:
                user_id = int(input("Enter an ID of a user: "))
            except ValueError:
                print("Please enter a valid ID. (e.g. 25)")
            else:
                break
        
        sql_query = """SELECT borrowed_book_id FROM users WHERE user_id = %s"""
        cursor.execute(sql_query, (user_id,))
        result = cursor.fetchone()
        
        if result is None or result[0] is None:
            print("The user doesn't have borrowed book")
            cursor.close()
            return
        
        book_id = result[0]
        
        book_return_query = """UPDATE books SET borrowed_by_user = NULL WHERE book_id = %s"""
        user_return_query = """UPDATE users SET borrowed_book_id = NULL, returned_at = CURRENT_TIMESTAMP WHERE user_id = %s"""
        cursor.execute(book_return_query, (book_id,))
        cursor.execute(user_return_query, (user_id,))
        
        connection.commit()
        cursor.close()
        print("Book returned")
        
    else:
        cursor.close()
        print("Invalid input")
        
def current_borrowings (connection):
    cursor = connection.cursor()
    
    query = """ SELECT * 
                FROM books 
                LEFT JOIN users ON books.book_id = users.borrowed_book_id;
            """
    
    cursor.execute(query)
    results = cursor.fetchall()


    if not results:
        print("No current borrowings found.")
    else:
        for row in results:
            print(row)
    
    cursor.close()

    