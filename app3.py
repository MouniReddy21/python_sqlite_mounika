import sqlite3

#Connect to a SQLite database file named (example3.db). 
#If this file doesn't exit, the file will be created
#sqlite3.connect returns a connection object, which provides methods to manage database connection
connection = sqlite3.connect('example3.db')
cursor = connection.cursor()

# Create a table 
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

try:
    # "BEGIN Transaction" starts a new transaction
    connection.execute('BEGIN TRANSACTION')

    # Insert into users
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 30))
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 25))

    # Commiting the transaction (if no error occurs)
    connection.commit()
    print("Transaction committed successfully.")

except sqlite3.Error as e:
    # if any error occurs, it is reversed to a state before the transaction begins
    print(f'Error: {e}')
    connection.rollback()
    print("Transaction rolled back.")

finally:
    # Close the connection
    connection.close()
