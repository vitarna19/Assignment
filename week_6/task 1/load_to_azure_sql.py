import sqlite3
import pandas as pd
from extract_from_local import extract_data

def load_data_to_sqlite(df):
    # Connect to SQLite DB (simulating Azure SQL)
    conn = sqlite3.connect("azure_sql_sim.db")
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    """)

    # Load data into table
    df.to_sql("customers", conn, if_exists='replace', index=False)

    print("Data loaded to simulated Azure SQL (SQLite DB).")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    df = extract_data()
    load_data_to_sqlite(df)
