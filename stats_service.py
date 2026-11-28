from database import expense_db
from datetime import datetime


def calculate_financial_stats(db_path='expense.db', start_date=None, end_date=None):
    total_income = expense_db.get_total_by_type('income', start_date, end_date)
    total_expense = expense_db.get_total_by_type('expense', start_date, end_date)
    balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }

def get_expense_by_category():
    return expense_db.get_expense_by_category()


def get_all_records():
    return expense_db.get_all_records()


def add_record(record_type, amount, category, record_date, note):
    return expense_db.add_record(record_type, amount, category, record_date, note)


def filter_records(category, start_date, end_date):
    return expense_db.filter_records(category, start_date, end_date)


def verify_login(username, password):
    return username == "admin" and password == "123456"


def add_record_with_validate(record_type, amount, category, record_date, note):
    if not amount or amount.strip() == '':
        raise ValueError("Amount cannot be empty")

    try:
        amount_num = float(amount)
    except ValueError:
        raise ValueError("Amount must be a valid number")

    if amount_num <= 0:
        raise ValueError("Amount must be greater than 0")

    from database.expense_db import add_record
    add_record(record_type, amount_num, category, record_date, note)


def get_filtered_records(category, start_date, end_date):
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

    from database.expense_db import filter_records
    return filter_records(category, start_date, end_date)