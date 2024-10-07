import sqlite3
from faker import Faker
import random

# Create a sqldatabase connection to company.db
connection = sqlite3.connect('company.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL,
    department_id INTEGER,
    manager_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id),
    FOREIGN KEY (manager_id) REFERENCES Employees(employee_id) 
)''') # self referencing foreign key, where manager_id is referencing to the primary key employee_id of the table Employees

cursor.execute('''
CREATE TABLE IF NOT EXISTS Projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Salaries (
    salary_id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    salary_amount REAL,
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
)''')



# Initialize Faker
fake = Faker()

# Generating sample data into the database company.db
def generate_departments(n):
    for _ in range(n):
        cursor.execute('''
        INSERT INTO Departments (department_id, department_name)
        VALUES (?, ?)''', (fake.unique.random_int(min=1, max=1000), fake.word().capitalize()))

def generate_employees(n):
    for _ in range(n):
        cursor.execute('''
        INSERT INTO Employees (employee_id, employee_name, department_id, manager_id)
        VALUES (?, ?, ?, ?)''', (
            fake.unique.random_int(min=1, max=1000),
            fake.name(),
            random.randint(1, 10),  # here i am assuming to have at least 10 departments
            random.choice([None, random.randint(1, n)])  # Random manager ID
        ))

def generate_projects(n):
    for _ in range(n):
        cursor.execute('''
        INSERT INTO Projects (project_id, project_name, department_id)
        VALUES (?, ?, ?)''', (
            fake.unique.random_int(min=1, max=1000),
            fake.word().capitalize(),
            random.randint(1, 10)
        ))

def generate_salaries(n):
    for _ in range(n):
        cursor.execute('''
        INSERT INTO Salaries (salary_id, employee_id, salary_amount)
        VALUES (?, ?, ?)''', (
            fake.unique.random_int(min=1, max=1000),
            random.randint(1, n),
            round(random.uniform(40000, 120000), 2)  # Salary between $40,000 and $120,000
        ))

generate_departments(10)
generate_employees(100)
generate_projects(30)
generate_salaries(100)

# Commiting the changes and closing the connection
connection.commit()
connection.close()

print("Database created and populated with sample data.")
