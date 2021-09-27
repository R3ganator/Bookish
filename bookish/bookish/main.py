import sqlite3

try:
    conn = sqlite3.connect('database.db')
except Error as e:
    print(e)

conn.close()