import sqlite3

def connect_db():
    return sqlite3.connect('example.db')

def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
    (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

def insert_record(cursor, name, age):
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

def display_records(cursor):
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    conn = connect_db()
    cursor = conn.cursor()
    
    create_table(cursor)
    
    # Get user input
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    
    insert_record(cursor, name, age)
    conn.commit()
    
    print("Records in the database:")
    display_records(cursor)
    
    conn.close()

if __name__ == "__main__":
    main()
