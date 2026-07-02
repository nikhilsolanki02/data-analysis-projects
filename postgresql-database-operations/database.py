# 1. importing psycopg library to connect to PostgreSQL database

import psycopg

# connecting to the database

connect = psycopg.connect(
    dbname="postgres",
    user="postgres",
    password="5128",
    host="localhost",
    port="5433")

cursor = connect.cursor()
print("Database is connected!")

# creating a database
def create_database():
    connect = psycopg.connect(
        dbname="postgres",
        user="postgres",
        password="5128",
        host="localhost",
        port="5433")
    connect.autocommit = True
    cursor = connect.cursor()
    cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'mydatabase'")
    if not cursor.fetchone():
        cursor.execute("CREATE DATABASE mydatabase")  
        print("Database created successfully!")       
    else:
        print("Database already exists!")             
    cursor.close()
    connect.close()

# creating a table

def create_table():
    connect = psycopg.connect(
    dbname="mydatabase",
    user="postgres",
    password="5128",
    host="localhost",
    port="5433")
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mytable (id int, name text, age int)")
    print("Table created successfully!")
    connect.commit()
    cursor.close()
    connect.close()

# inserting data into the table

def insert_data():
    connect = psycopg.connect(
    dbname="mydatabase",
    user="postgres",
    password="5128",
    host="localhost",
    port="5433")
    cursor = connect.cursor()
    cursor.execute( '''INSERT INTO mytable (id, name, age) VALUES (5, 'John', 30)''')
    cursor.execute( '''INSERT INTO mytable (id, name, age) VALUES (6, 'Bob', 25)''')
    print("Data inserted successfully!")
    connect.commit()
    cursor.close()
    connect.close()

# fetching data from the table

def fetch_data():
    connect = psycopg.connect(
    dbname="mydatabase",
    user="postgres",
    password="5128",
    host="localhost",
    port="5433")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM mytable")
    print(cursor.fetchall())
    print("Data fetched successfully!")
    connect.commit()
    cursor.close()
    connect.close()

# inserting user input data into the table

def insert_user_data():
    connect = psycopg.connect(
    dbname="mydatabase",
    user="postgres",
    password="5128",
    host="localhost",
    port="5433")
    cursor = connect.cursor()
    id = input("Enter user id: ")
    name = input("Enter user name: ")
    age = input("Enter user age: ")
    query = ('''INSERT INTO mytable (id, name, age) VALUES (%s, %s, %s)''')
    cursor.execute(query, (id, name, age))
    print("User input inserted successfully!")
    connect.commit()
    cursor.close()
    connect.close()

# fetching user input data from the table

def fetch_user_data():
    connect = psycopg.connect(
    dbname="mydatabase",
    user="postgres",
    password="5128",
    host="localhost",
    port="5433")
    cursor = connect.cursor()
    id = input("Enter user id: ")
    cursor.execute("SELECT * FROM mytable WHERE id = %s", (id,))
    print(cursor.fetchall())
    print("User data fetched successfully!")
    connect.commit()
    cursor.close()
    connect.close()

# clearing the table

def clear_table():
    connect = psycopg.connect(
    dbname="mydatabase",
    user="postgres",
    password="5128",
    host="localhost",
    port="5433")
    cursor = connect.cursor()
    cursor.execute("TRUNCATE TABLE mytable")
    print("Table cleared successfully!")
    connect.commit()
    cursor.close()
    connect.close()

create_database()
create_table()
insert_data()
fetch_data()
insert_user_data()
fetch_user_data()
clear_table()