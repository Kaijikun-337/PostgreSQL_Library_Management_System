def delete_book (connection):
    cursor = connection.cursor()
    book_id = input("Enter book's ID: ")
    
    query = """SELECT borrowed_by_user FROM books WHERE book_id = %s"""
    cursor.execute(query, (book_id,))
    result = cursor.fetchone()
    
    if result is None:
        cursor.close()
        print("No book found")
        return
    elif result[0]:
        user_id = result[0]
        query = """UPDATE users SET borrowed_book_id = NULL WHERE user_id = %s"""
        cursor.execute(query, (user_id,))
        query = """DELETE FROM books WHERE book_id = %s"""
        cursor.execute(query, (book_id,))
    else:
        query = """DELETE FROM books WHERE book_id = %s"""
        cursor.execute(query, (book_id,))
    
    cursor.close()
    connection.commit()
    
def delete_user (connection):
    cursor = connection.cursor()
    user_id = input("Enter user's ID: ")
    
    query = """SELECT borrowed_book_id FROM users WHERE user_id = %s"""
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    
    if result is None:
        cursor.close()
        print("No user found")
        return
    elif result[0]:
        book_id = result[0]
        query = """UPDATE books SET borrowed_by_user = NULL WHERE book_id = %s"""
        cursor.execute(query, (book_id,))
        
        query = """DELETE FROM users WHERE user_id = %s"""
        cursor.execute(query, (user_id,))
    else:
        query = """DELETE FROM users WHERE user_id = %s"""
        cursor.execute(query, (user_id,))
    
    cursor.close()
    connection.commit()
