
import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).resolve().parent.parent / "notebridge.db"

conn = sqlite3.connect(DATABASE_PATH)

print("Database connected successfully!")

tables = conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
).fetchall()

print("\nTables in database:")

for table in tables:
    print(table[0])

print("\nDocuments table structure:")

columns = conn.execute(
    "PRAGMA table_info(documents)"
).fetchall()

for column in columns:
    print(column)

print("\nStored documents:")

documents = conn.execute(
    "SELECT * FROM documents"
).fetchall()

for document in documents:
    print(document)

conn.close()
