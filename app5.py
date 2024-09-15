import sqlite3

# Connect to the database
connection = sqlite3.connect('example5.db')
cursor = connection.cursor()

# Create a table with a BLOB column
cursor.execute('CREATE TABLE IF NOT EXISTS files (id INTEGER PRIMARY KEY, data BLOB)')

# Insert binary data into the table
with open('image1.jpg', 'rb') as file:
    blob_data = file.read()
    cursor.execute('INSERT INTO files (data) VALUES (?)', (blob_data,))

# Commit the transaction
connection.commit()

# Retrieve binary data from the table
cursor.execute('SELECT data FROM files WHERE id = 1')
blob_data = cursor.fetchone()[0]

# Save the retrieved binary data to a file
with open('retrieved_image.png', 'wb') as file:
    file.write(blob_data)

# Close the connection
connection.close()
