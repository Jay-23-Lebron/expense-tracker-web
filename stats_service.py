from database import expense_db


def calculate_financial_stats(db_path='expense.db', start_date=None, end_date=None):
    total_income = expense_db.get_total_by_type('income', start_date, end_date)
    total_expense = expense_db.get_total_by_type('expense', start_date, end_date)
    balance = total_income - total_expense

    return {
        "total_incoome": total_income,
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