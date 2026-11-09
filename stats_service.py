import sqlite3

def get_db_connection():
    conn = sqlite3.connect('expense.db')
    conn.row_factory = sqlite3.Row
    return conn

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


def get_expense_by_category():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT category, SUM(amount) as total
            FROM expense
            WHERE type = 'expense'
            GROUP BY category
        """)
        rows = cursor.fetchall()

        category_stats = []
        for row in rows:
            category_stats.append({
                "category": row["category"],
                "total": row["total"]
            })

    except Exception as e:
        print(f"Category stats error: {e}")
        return []
    finally:
        conn.close()

    return category_stats


def get_all_records():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT id, type, amount, category, note, created_at FROM expense')
    records = cursor.fetchall()
    cursor.close()
    conn.close()

    return records


def add_record(record_type, amount, category, record_date, note):
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        insert_sql = """
            INSERT INTO expense (type, amount, category, date, note)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(insert_sql, (record_type, amount, category, record_date, note))
        conn.commit()
        return True

    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def filter_records(category, start_date, end_date):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "SELECT id, type, amount, category, note, date FROM expense WHERE 1=1 "
    params = []

    if category and category.strip():
        sql += " AND category = ?"
        params.append(category)

    if start_date and not end_date:
        sql += " AND date >= ?"
        params.append(start_date)

    if end_date and not start_date:
        sql += " AND date <= ?"
        params.append(end_date)

    if start_date and end_date:
        sql += " AND date BETWEEN ? AND ?"
        params.append(start_date)
        params.append(end_date)

    cursor.execute(sql, params)
    records = cursor.fetchall()

    cursor.close()
    conn.close()
    return records