import sqlite3
import json
from pathlib import Path

data_dir = Path.cwd() / 'data'
db_dir = Path.cwd() / 'app/db'
create_tables_path = db_dir / 'create_tables.sql'
db_path = data_dir / 'gears_and_grimoires.db'

conn = sqlite3.connect(str(db_path))
cursor = conn.cursor()

cursor.executescript(create_tables_path.read_text())

conn.commit()

# Function to insert JSON data into a table
def insert_data(table, data):
    columns = ", ".join(data.keys())
    placeholders = ", ".join(["?"] * len(data))
    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    cursor.execute(sql, tuple(data.values()))