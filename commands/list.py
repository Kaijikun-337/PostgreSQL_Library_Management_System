def list_users(connection):
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM users")    
    
    results = cursor.fetchall()
    
    if not results:
        print("The table is empty.")
    else:
        for user_id, full_name, borrowed_book_id, borrowed_at, returned_at in results:
            print(f"ID: {user_id} | Name: {full_name} | Borrowed book ID: {borrowed_book_id} | Borrowed date: {borrowed_at} | Returned date: {returned_at}")
    
    cursor.close()
        
        
        
def list_books(connection):
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM books")
        
    results = cursor.fetchall()
    
    if not results:
        print("The table is empty.")
    else:
        for book_id, title, author, genre, borrowed_by_user in results:
            print(f"ID: {book_id} | Title: {title} | Author: {author} | Genre: {genre} | Borrowed by user: {borrowed_by_user}")

    
    cursor.close()
    