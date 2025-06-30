import sqlite3

conn = sqlite3.connect("source.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, score INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS teachers (id INTEGER, name TEXT, subject TEXT)")

cursor.execute("INSERT INTO students VALUES (1, 'Alice', 85), (2, 'Bob', 90)")
cursor.execute("INSERT INTO teachers VALUES (101, 'Mr. Smith', 'Math'), (102, 'Ms. Rose', 'Science')")

conn.commit()
conn.close()

print("✔ Sample source.db created with 2 tables.")
