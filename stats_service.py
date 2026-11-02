import sqlite3

def calculate_financial_stats(db_path='expense.db', start_date=None, end_date=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    income_sql = "SELECT SUM(amount) FROM expense WHERE type = ?"
    params = ['income']

    if start_date:
        income_sql += " AND date >= ?"
        params.append(start_date)
    if end_date:
        income_sql += " AND date <= ?"
        params.append(end_date)

    cursor.execute(income_sql, params)
    total_income = cursor.fetchone()[0]
    if total_income is None:
        total_income = 0

    expense_sql = "SELECT SUM(amount) FROM expense WHERE type = ?"
    params = ['expense']

    if start_date:
        expense_sql += " AND date >= ?"
        params.append(start_date)
    if end_date:
        expense_sql += " AND date <= ?"
        params.append(end_date)

    cursor.execute(expense_sql, params)
    total_expense = cursor.fetchone()[0]
    if total_expense is None:
        total_expense = 0


    balance = total_income - total_expense

    conn.close()

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }
