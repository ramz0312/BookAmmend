import sqlite3
from sqlite3 import Error

DATABASE_FILE = 'bookammend.db'

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def setup_database(conn):
    try:
        cursor = conn.cursor()
        
        # Table 1: Books (Stores metadata)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Books (
                book_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                genre TEXT NOT NULL,
                synopsis TEXT
            );
        """)
        
        # Table 2: Users (For personalized history)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                user_id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        """)
        
        # Table 3: ReadingHistory (For personalized recommendations)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ReadingHistory (
                history_id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES Users (user_id),
                FOREIGN KEY (book_id) REFERENCES Books (book_id)
            );
        """)
        conn.commit()
        print("Database tables created successfully.")
    except Error as e:
        print(f"Error setting up tables: {e}")

def fetch_books_by_genre(conn, genre):
    """Placeholder function to fetch books based on genre."""
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, genre FROM Books WHERE genre = ? LIMIT 10;", (genre,))
    return cursor.fetchall()

if __name__ == '__main__':
    conn = create_connection()
    if conn:
        setup_database(conn)
      
