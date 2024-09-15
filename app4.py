import sqlite3

# Row factory function that converts rows to dictionaries
def dict_factory(cursor, row):
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

#Connect to a SQLite database file named (example3.db). 
#If this file doesn't exit, the file will be created
#sqlite3.connect returns a connection object, which provides methods to manage database connection
connection = sqlite3.connect('example4.db')

connection.row_factory = dict_factory  # Set the row factory

# Cursor creation
cursor = connection.cursor()

# Create a table
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

# Insert data
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Mounika', 23))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Shriya', 22))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Tom', 25))

# Query the database
cursor.execute('SELECT * FROM users')

# Fetching all rows
rows = cursor.fetchall()

# Printing results
for row in rows:
    print(row)  # Each row is a dictionary with column names as keys

# Closing the connection
connection.close()
