import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import fastavro
import sqlite3

# Step 1: Connect to relational database (SQLite in this case)
conn = sqlite3.connect("student.db")
query = "SELECT * FROM students"
df = pd.read_sql_query(query, conn)
conn.close()

# Step 2: Export to CSV (broad compatibility)
df.to_csv("data.csv", index=False)
print("✔ Exported to data.csv")

# Step 3: Export to Parquet (efficient analytics)
table = pa.Table.from_pandas(df)
pq.write_table(table, "data.parquet")
print("✔ Exported to data.parquet")

# Step 4: Export to Avro (schema evolution, compact serialization)
records = df.to_dict(orient="records")
schema = {
    "doc": "Student scores data",
    "name": "StudentRecord",
    "namespace": "example.avro",
    "type": "record",
    "fields": [
        {"name": "id", "type": ["null", "int"]},
        {"name": "name", "type": ["null", "string"]},
        {"name": "score", "type": ["null", "int"]}
    ]
}
with open("data.avro", "wb") as out_avro:
    fastavro.writer(out_avro, schema, records)
print("✔ Exported to data.avro")
