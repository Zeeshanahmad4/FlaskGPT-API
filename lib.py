import csv
import re
import sqlite3

# Connect to the SQLite database


def log_message(user_id, chat_id, role, message,deviceid,date):
      conn = sqlite3.connect('chat.db', isolation_level=None)
      cursor = conn.cursor()
     
      cursor.execute('''
        INSERT INTO users (userid, chatid, role, response, deviceid, date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, chat_id, role, message,deviceid,date))
      conn.commit()
def get_user_data(user_id,chat_id):
    conn = sqlite3.connect('chat.db', isolation_level=None)
    cursor = conn.cursor()
   
    cursor.execute('''
    SELECT role, response FROM users WHERE userid = ? AND chatid = ?
    ''', (user_id, chat_id))
    return cursor.fetchall()

def get_user_data_free_paid(user_id,deviceid,date):
    conn = sqlite3.connect('chat.db', isolation_level=None)
    cursor = conn.cursor()
   
    cursor.execute('''
    SELECT * FROM users WHERE userid = ? AND deviceid = ? AND date = ?
    ''', (user_id,deviceid,date))
    
    data = cursor.fetchall()
    num_rows = len(data)
    return num_rows
  
def checkuserauthenticate(email,password):
  conn = sqlite3.connect('chat.db', isolation_level=None)
  cursor = conn.cursor()
  cursor.execute("SELECT COUNT(*) FROM usersauth WHERE email = ? AND password = ?", (email, password))
  result = cursor.fetchone()

# Check if the user exists
  if result[0] > 0:
    return 1
  else:
    return 0

# Close the connection
  conn.close()
def validate_email(email):
    # Regular expression pattern for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None
def createusers(firstname,lastname,email,password):
  conn = sqlite3.connect('chat.db', isolation_level=None)
  cursor = conn.cursor()
  cursor.execute("SELECT COUNT(*) FROM usersauth WHERE email = ?", (email,))
  result = cursor.fetchone()
  if result[0] > 0:
    return 2
  else:
    if validate_email(email):
      cursor.execute("INSERT INTO usersauth (first_name, last_name, email, password) VALUES (?, ?, ?, ?)",
                       (firstname, lastname, email, password))
      conn.commit()
      conn.close()
      return 1
      
    else:
      return 0
  
