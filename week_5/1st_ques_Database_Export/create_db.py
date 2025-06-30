import sqlite3

# Connect to SQLite DB (will create file if it doesn't exist)
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    score INTEGER
)
""")

# Insert sample records
cursor.executemany("""
INSERT INTO students (id, name, score) VALUES (?, ?, ?)
""", [
    (1, 'Alice', 85),
    (2, 'Bob', 90),
    (3, 'Charlie', 95)
])

conn.commit()
conn.close()

print("Database created with sample data.")
