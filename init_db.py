import sqlite3
conn = sqlite3.connect('expense.db')
cursor = conn.cursor()

create_table_sql = """
CREATE TABLE IF NOT EXISTS expense (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    date TEXT NOT NULL,
    note TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""
cursor.execute(create_table_sql)

insert_sample_sql = """
INSERT INTO expense (type, amount, category, date, note)
VALUES ('expense', 35.5, 'food', '2026-10-16', 'lunch')
"""
cursor.execute(insert_sample_sql)

conn.commit()
conn.close()