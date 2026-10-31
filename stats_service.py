import sqlite3

def calculate_financial_stats(db_path='expense.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expense WHERE type = 'income'")
    total_income = cursor.fetchone()[0]
    if total_income is None:
        total_income = 0

    cursor.execute("SELECT SUM(amount) FROM expense WHERE type = 'expense'")
    total_expense = cursor.fetchone()[0]
    if total_income is None:
        total_income = 0

    balance = total_income - total_expense

    conn.close()

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }
