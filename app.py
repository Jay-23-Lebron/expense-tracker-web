from flask import Flask, render_template, request, redirect, jsonify, session
import sqlite3
from datetime import datetime
import stats_service
from stats_service import calculate_financial_stats, get_expense_by_category
app = Flask(__name__)
app.secret_key = "your_test_secret_key_123456"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')

    if username == "admin" and password == "123456":
        session['username'] = username
        return redirect('/')
    else:
        return render_template('login.html', error="Invalid username or password")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

@app.route('/')
def index():
    if 'username' not in session:
        return redirect('/login')

    records = stats_service.get_all_records()
    return render_template('dashboard.html', records=records)

@app.route('/add-record')
def add_record_page():
    if 'username' not in session:
        return redirect('/login')

    return render_template('expense-form.html')

@app.route('/add-record', methods=['GET', 'POST'])
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
       stats_service.add_record(record_type, amount_num, category, record_date, note)

    except Exception as e:
        return f'Error: Failed to save record. {str(e)}'

    return redirect('/')

@app.route('/filter')
def filter_records():
    category = request.args.get('category')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if start_date:
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            start_date = ""

    if end_date:
        try:
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            end_date = ""

    records = stats_service.filter_records(category, start_date, end_date)

    return render_template('filter.html', 
                           records=records,
                           selected_category=category,
                           start_date=start_date,
                           end_date=end_date)


@app.route('/api/stats')
def stats_api():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    try:
        stats = calculate_financial_stats(start_date=start_date, end_date=end_date)
        return jsonify(stats)

    except Exception as e:
        return jsonify({
            "error": "Failed to fetch statistics",
            "details": str(e)
        }), 500

@app.route('/api/expense-by-category')
def expense_by_category():
    category_stats = get_expense_by_category()
    return jsonify(category_stats)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

