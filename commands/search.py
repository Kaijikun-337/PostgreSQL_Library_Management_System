def search_book(connection):
    cursor = connection.cursor()
    
    while True:
        print("1. By book ID")
        print("2. By book title")
        print("3. By book author")
        print("0. Back to main menu")
        
        choice = input("Choose any of these: ")
        
        if choice == "1":
            
            while True:
                try:
                    book_id = int(input("Please enter an ID: "))
                except ValueError:
                    print("Please enter a valid ID. (e.g. 25)")
                else:
                    break
            
            query = "SELECT * FROM books WHERE book_id = %s"
            cursor.execute(query, (book_id,))
            
            result = cursor.fetchone()

            if not result:
                print("No books found.")
            else:
                print(result)

                
            
        elif choice == "2":
            title = input("Please enter a book title: ").strip()
            
            query = "SELECT * FROM books WHERE title ILIKE %s"
            cursor.execute(query, (title,))
            
            results = cursor.fetchall()

            if not results:
                print("No books found.")
            else:
                for row in results:
                    print(row)

        
        elif choice == "3":
            author = input("Please enter a book author: ").strip()
            
            query = "SELECT * FROM books WHERE author ILIKE %s"
            cursor.execute(query, (author,))
            
            results = cursor.fetchall()

            if not results:
                print("No books found.")
            else:
                for row in results:
                    print(row)

        
        elif choice == "0":
            cursor.close()
            break
        
        else:
            print("Invalid input")