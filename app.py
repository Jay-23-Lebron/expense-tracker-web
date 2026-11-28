from flask import Flask, render_template, request, redirect, jsonify, session, Response
from datetime import datetime
import stats_service
import csv
import io

app = Flask(__name__)
app.secret_key = "your_test_secret_key_123456"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')

    if stats_service.verify_login(username, password):
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

    try:
        stats_service.add_record_with_validate(record_type, amount, category, record_date, note)
    except ValueError as e:
        return f'Error: {str(e)}'

    except Exception as e:
        return f'Error: Failed to save record. {str(e)}'

    return redirect('/')

@app.route('/filter')
def filter_records():
    category = request.args.get('category')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    records = stats_service.get_filtered_records(category, start_date, end_date)

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
        stats = stats_service.calculate_financial_stats(start_date=start_date, end_date=end_date)
        return jsonify(stats)

    except Exception as e:
        return jsonify({
            "error": "Failed to fetch statistics",
            "details": str(e)
        }), 500

@app.route('/api/expense-by-category')
def expense_by_category():
    category_stats = stats_service.get_expense_by_category()
    return jsonify(category_stats)

@app.route('/export')
def export_records():
    if 'username' not in session:
        return redirect('/login')

    records = stats_service.get_all_records()

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(['ID', 'Type', 'Amount', 'Category', 'Date', 'Note'])

    for record in records:
        writer.writerow([
            record['id'],
            record['type'],
            record['amount'],
            record['category'],
            record['date'],
            record['note']
        ])

    csv_content = output.getvalue()
    output.close()

    response = Response(csv_content, mimetype='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename="expense_records.csv"'

    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)

