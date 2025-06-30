import sqlite3

# Connect to source and destination
source_conn = sqlite3.connect("source.db")
dest_conn = sqlite3.connect("destination.db")

source_cursor = source_conn.cursor()
dest_cursor = dest_conn.cursor()

# Step 1: Get all table names from source DB
source_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = source_cursor.fetchall()

for (table_name,) in tables:
    print(f"🔄 Copying table: {table_name}")

    # Step 2: Get create statement for the table
    source_cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    create_stmt = source_cursor.fetchone()[0]

    # Step 3: Create same table in destination
    dest_cursor.execute(create_stmt)

    # Step 4: Copy all data
    source_cursor.execute(f"SELECT * FROM {table_name}")
    rows = source_cursor.fetchall()

    if rows:
        placeholders = ','.join(['?'] * len(rows[0]))
        insert_stmt = f"INSERT INTO {table_name} VALUES ({placeholders})"
        dest_cursor.executemany(insert_stmt, rows)

dest_conn.commit()
source_conn.close()
dest_conn.close()

print("✅ All tables copied from source.db to destination.db")


import sqlite3

conn = sqlite3.connect("destination.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

for (t,) in tables:
    print(f"\n📋 Table: {t}")
    cursor.execute(f"SELECT * FROM {t}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

conn.close()
