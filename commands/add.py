import psycopg2

def add_user(connection):
    cursor = connection.cursor()
    
    while True:
        name = input("Insert a full name of a new user: ")

        if name.strip() != "":
            break
        
        print("Invalid name.")
    
    query = """INSERT INTO users (full_name) VALUES(%s);"""
    
    try:
        cursor.execute(query, (name,))
        connection.commit()
    except psycopg2.Error as e:
        print(f"The error '{e}' occurred")
        connection.rollback()
    else:
        print(name + " is added!")
    finally:
        cursor.close()        
    

    
def add_book(connection):
    cursor = connection.cursor()
    
    while True:
        title = input("Insert a title of a new book: ")
    
        if title.strip() != "":
            break
        
        print("Invalid title.")
        
    author = input("Insert an author of the book: ")
    genre = input("Insert a genre of the book: ")
    query = """INSERT INTO books (title, author, genre) VALUES(%s, %s, %s);"""
    
    try:
        cursor.execute(query, (title, author, genre))
        connection.commit()
    except psycopg2.Error as e:
        print(f"The error '{e}' occurred")
        connection.rollback()
    else:
        print(title + " is added!")
    finally:
        cursor.close() 
    
    