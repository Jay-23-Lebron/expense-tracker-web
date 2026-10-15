from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/home')
def home():
    return "This is the /home page"

@app.route('/about')
def about():
    return "This is the /about page"

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

    print('--- Received Form Data ---')
    print(f'Type: {record_type}')
    print(f'Amount: {amount}')
    print(f'Category: {category}')
    print(f'Date: {record_date}')
    print(f'Note: {note}')
    print('--------------------------')

    return 'Form submitted successfully'

@app.route('/user/<username>')
def user_profile(username):
    return render_template('user-profile-demo.html', username=username)

if __name__ == '__main__':
    app.run(debug=True, port=5000)