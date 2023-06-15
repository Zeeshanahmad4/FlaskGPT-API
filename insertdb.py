import sqlite3

# Connect to the database
conn = sqlite3.connect('chat.db')
cursor = conn.cursor()

# Insert specific data into the users table
first_name = "Awais"
last_name = "Ahmad"
email = "user@gmail.com"
password = "user123"

cursor.execute("INSERT INTO usersauth (first_name, last_name, email, password) VALUES (?, ?, ?, ?)",
               (first_name, last_name, email, password))

# Commit the changes and close the connection
conn.commit()
conn.close()
