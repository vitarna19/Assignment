import sqlite3

# Connect to source and destination
source_conn = sqlite3.connect("source.db")
dest_conn = sqlite3.connect("destination.db")

source_cursor = source_conn.cursor()
dest_cursor = dest_conn.cursor()

# ✅ Define what to copy
# Format: { table_name: [column1, column2, ...] }
selection = {
    "students": ["id", "name"],              # omit 'score'
    "teachers": ["name", "subject"]          # omit 'id'
}

for table, columns in selection.items():
    cols_str = ", ".join(columns)

    print(f"🔄 Copying columns [{cols_str}] from table '{table}'")

    # 1. Get data from source
    source_cursor.execute(f"SELECT {cols_str} FROM {table}")
    rows = source_cursor.fetchall()

    # 2. Create table in destination
    col_defs = ", ".join([f"{col} TEXT" for col in columns])  # Simplified as TEXT
    dest_cursor.execute(f"DROP TABLE IF EXISTS {table}")
    dest_cursor.execute(f"CREATE TABLE {table} ({col_defs})")

    # 3. Insert data
    if rows:
        placeholders = ", ".join(["?"] * len(columns))
        insert_sql = f"INSERT INTO {table} VALUES ({placeholders})"
        dest_cursor.executemany(insert_sql, rows)

dest_conn.commit()
source_conn.close()
dest_conn.close()

print("✅ Selective migration complete!")
