from flask import Flask, render_template, request, redirect
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, type, amount, category, note, created_at FROM expense')
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('dashboard.html', records = records)

@app.route('/add-record')
def add_record_page():
    return render_template('expense-form.html')

@app.route('/add-record', methods=['POST'])
def add_record_submit():
    record_type = request.form.get('type')
    amount = request.form.get('amount')
    category = request.form.get('category')
    record_date = request.form.get('date')
    note = request.form.get('note')

    if not amount or amount.strip() == '':
        return 'Error: Amount cannot be empty'

    try:
        amount_num = float(amount)
    except ValueError:
        return 'Error: Amount must be a valid number'

    if amount_num <= 0:
        return 'Error: Amount must be greater than 0'

    try:
        conn = sqlite3.connect('expense.db')
        cursor = conn.cursor()

        insert_sql = """
            INSERT INTO expense (type, amount, category, date, note)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(insert_sql, (record_type, amount_num, category, record_date, note))
        conn.commit()

    except Exception as e:
        conn.rollback()
        return f'Error: Failed to save record. {str(e)}'

    finally:
        if conn:
            cursor.close()
            conn.close()

    return redirect('/')

@app.route('/filter')
def filter_records():
    category = request.args.get('category')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()

    sql = "SELECT id, type, amount, category, note, date FROM expense WHERE 1=1 "
    params = []

    if category and category.strip():
        sql += " AND category = ?"
        params.append(category)

    if start_date and end_date:
        sql += " AND date BETWEEN ? AND ?"
        params.append(start_date)
        params.append(end_date)

    cursor.execute(sql, params)
    records = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return str(records)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

