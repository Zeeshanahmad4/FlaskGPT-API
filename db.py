import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('chat.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        userid TEXT,
        chatid INTEGER,
        role TEXT,
        response TEXT,
        deviceid TEXT,
        date DATE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usersauth (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
''')