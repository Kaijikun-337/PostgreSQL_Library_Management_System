import os
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv

load_dotenv()

DB_NAME=os.getenv("DB_NAME")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")

connection = None
try:
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )
    print("Connection to PostgreSQL DB successful")
except OperationalError as e:
    print(f"The error '{e}' occurred")
else:
    cursor = None
    try:
        cursor = connection.cursor()
        
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users
                    (
                        user_id SERIAL PRIMARY KEY,
                        full_name VARCHAR(255) NOT NULL,
                        borrowed_book_id INTEGER,
                        borrowed_at DATE,
                        returned_at DATE
                    );
                    ''')
        
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS books
                    (
                        book_id SERIAL PRIMARY KEY,
                        title VARCHAR(255) NOT NULL,
                        author VARCHAR(255),
                        genre VARCHAR(255),
                        borrowed_by_user INTEGER REFERENCES users(user_id)     
                    ) 
                    ''')
        
        cursor.execute("""
            SELECT 1
            FROM pg_constraint
            WHERE conname = 'adding_fkey_for_borrowed_book_id'
        """)

        constraint_exists = cursor.fetchone()

        if constraint_exists is None:
            cursor.execute('''
                ALTER TABLE users
                ADD CONSTRAINT adding_fkey_for_borrowed_book_id
                FOREIGN KEY (borrowed_book_id)
                REFERENCES books(book_id)
            ''')

        
        connection.commit()
    except psycopg2.Error as e:
        print(f"The error '{e}' occurred")
        connection.rollback()
    finally:
        if cursor is not None:
            cursor.close()
        
        if connection is not None:
            connection.close()
            
def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )