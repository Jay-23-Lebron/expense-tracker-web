import sqlite3
conn = sqlite3.connect('expense.db')
cursor = conn.cursor()

create_table_sql = """
CREATE TABLE IF NOT EXISTS expense (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    note TEXT,
    created_at TEXT NOT NULL
)
"""

cursor.execute(create_table_sql)
insert_sql = """
INSERT INTO expense (type, amount, category, note, created_at)
VALUES ('expense', 35.5, 'food', 'lunch', '2026-10-13 12:30:00')
"""
cursor.execute(insert_sql)

cursor.execute("SELECT * FROM expense")
result = cursor.fetchall()
print("Records in database:", result)

conn.commit()
conn.close()