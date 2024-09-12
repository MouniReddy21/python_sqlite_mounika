#sqlite3 module, a built-in python library to work with SQLite database
import sqlite3

#Connect to a SQLite database file named (example2.db). 
#If this file doesn't exit, the file will be created
#sqlite3.connect returns a connection object, which provides methods to manage database connection
connection = sqlite3.connect('example2.db')

#create a curser object from the connection object, 
#which is used to execute SQL commands and queries like fetching and execution against the database
cursor = connection.cursor()

#Creating a table students in the example2 database using cursor.execute()

#1 Handling the error by using try-catch block
# try:
#     cursor.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, grade REAL)")
# except sqlite3.OperationalError as e:
#     print(f"An error occured: {e}")

#2 using if not exist for creating table
#cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade REAL)")

#3 By dropping the table if it already exists and creating the new table
# Drop the table if it exists
cursor.execute("DROP TABLE IF EXISTS students")

# Create the table
cursor.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, grade REAL)")


#inserting a new record into that students table
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ('Mounika', 86.5))
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ('Alice', 85.5))

#To retrive all the records from the students table
cursor.execute("SELECT * FROM students")

#To fetch data from the last executed query using cursor.fetchall()
rows = cursor.fetchall()
for row in rows:
    print(row)

#commit the changes to the database
connection.commit()

#close the connection to the database
connection.close()





