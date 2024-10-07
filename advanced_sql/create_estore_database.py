import sqlite3
from faker import Faker
import random

# Creating a sqldatabase connection to Estore.db
connection = sqlite3.connect('Estore.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_name TEXT NOT NULL,
    order_date TEXT NOT NULL,
    product_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Suppliers (
    supplier_id INTEGER PRIMARY KEY,
    supplier_name TEXT NOT NULL
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Product_suppliers (
    product_id INTEGER,
    supplier_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
)''')

# Initialize Faker
fake = Faker()

# Generating the sample data into the data database Estore.db
def generate_customers(n):
    for _ in range(n):
        cursor.execute('''
        INSERT INTO Customers (customer_id, customer_name)
        VALUES (?, ?)''', (fake.unique.random_int(min=1, max=1000), fake.name()))

def generate_products(n):
    for _ in range(n):
        cursor.execute('''
        INSERT INTO Products (product_id, product_name)
        VALUES (?, ?)''', (fake.unique.random_int(min=1, max=1000), fake.word()))

def generate_orders(n):
    for _ in range(n):
        cursor.execute('''
        INSERT INTO Orders (order_id, customer_id, product_name, order_date, product_id)
        VALUES (?, ?, ?, ?, ?)''', (
            fake.unique.random_int(min=1, max=1000),
            random.randint(1, 100),
            fake.word(),
            fake.date(),
            random.randint(1, 100)
        ))

def generate_suppliers(n):
    for _ in range(n):
        cursor.execute('''
        INSERT INTO Suppliers (supplier_id, supplier_name)
        VALUES (?, ?)''', (fake.unique.random_int(min=1, max=1000), fake.company()))

def generate_product_suppliers(n):
    for _ in range(n):
        cursor.execute('''
        INSERT INTO Product_suppliers (product_id, supplier_id)
        VALUES (?, ?)''', (
            random.randint(1, 100),
            random.randint(1, 20)
        ))

generate_customers(100)
generate_products(50)
generate_orders(200)
generate_suppliers(20)
generate_product_suppliers(50)

# Commiting the changes and closing the connection
connection.commit()
connection.close()

print("Database created and populated with sample data.")
