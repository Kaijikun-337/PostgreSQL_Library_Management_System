```
# PostgreSQL Library Management System

A small library-management application written in Python using PostgreSQL and `psycopg2`.

The application allows users to manage library users and books, search for books, borrow and return books, view current borrowings, and delete users or books.

## Features

- Add users
- Add books
- List users
- List books
- Search books by:
  - Book ID
  - Title
  - Author
- Borrow books
- Return books by book ID or user ID
- Show current borrowings
- Delete users
- Delete books

## Project Structure

```
library-project/
├── main.py
├── commands/
│   ├── add.py
│   ├── borrow_and_return.py
│   ├── delete.py
│   ├── list.py
│   └── search.py
├── database/
│   └── db.py
├── .env
├── .gitignore
└── README.md
```

## Requirements

- Python 3
- PostgreSQL
- The following Python packages:

```
psycopg2-binary
python-dotenv
```

Install the packages with:

```
pip install psycopg2-binary python-dotenv
```

## Database Configuration

Create a `.env` file in the project’s main folder:

```
DB_NAME=your_database_name
DB_USER=your_postgresql_username
DB_PASSWORD=your_postgresql_password
DB_HOST=localhost
DB_PORT=5432
```

The application creates the `users` and `books` tables when the database connection is initialized.

## Running the Application

From the project’s main folder, run:

```
python main.py
```

The application will display a menu:

```
1. Add user
2. Add book
3. List users
4. List books
5. Search books
6. Borrow book
7. Return book
8. Show current borrowings
9. Delete user
10. Delete book
0. Exit
```

Enter the number of the action you want to perform.

## Database Design

The project uses two tables.

### Users

- `user_id`
- `full_name`
- `borrowed_book_id`
- `borrowed_at`
- `returned_at`

### Books

- `book_id`
- `title`
- `author`
- `genre`
- `borrowed_by_user`

Each user can have one active borrowed book, and each book can be borrowed by one user.

## Current Limitations

- A user can borrow only one book at a time.
- The database does not preserve a complete borrowing history.
- Deleting a borrowed book or user clears the borrowing relationship.
- Book searches by title and author currently use case-insensitive matching.
```

Also make sure your `.gitignore` contains:

```
.env
__pycache__/
*.pyc
venv/
.venv/
```

The most important parts are the project description, features, installation instructions, database configuration, and run command. You don’t need a long or professional-looking README for this project—this is already enough.