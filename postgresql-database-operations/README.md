# Database Operations using Python

This project is part of my Python course assignment, where I practiced connecting Python to a PostgreSQL database and performing basic database operations using the psycopg library.

## What I built
I wrote Python scripts to:
- Connect to a PostgreSQL database
- Create a database and a table
- Insert records into the table
- Fetch and display data from the table
- Take user input and insert it using parameterized queries
- Filter data using SELECT with WHERE conditions
- Clear the table using TRUNCATE

## Libraries and Tools Used
- Python
- PostgreSQL
- psycopg (for database connection)
- VS Code (for writing code)

## How to Run

Step 1 - Install the required library:
```
pip install psycopg
```

Step 2 - Make sure PostgreSQL is installed and running on your system

Step 3 - Open `database.py` and update your PostgreSQL credentials:
```python
user = "your_username"
password = "your_password"
port = "your_port"
```

Step 4 - Run the script:
```
python database.py
```

## What I Learned
- How to connect Python with PostgreSQL using psycopg
- How to create databases and tables from Python
- How to insert and fetch data using a cursor.execute()
- How to use parameterized queries for user input
- How to use connect.commit() and connect.close() properly

## Author
Nikhil Solanki
BTech Final Year - AI & Data Science
GitHub: https://github.com/nikhilsolanki02
