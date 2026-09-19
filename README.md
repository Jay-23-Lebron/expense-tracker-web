# Expense Tracker Web
A full-stack personal income & expense management web application, built as a portfolio project for IT career development.

## Current Progress
✅ **Phase 1 - Static HTML Foundation (Completed)**
- Built static transaction creation form with core fields:
  - Transaction type dropdown (Income / Expense)
  - Number input for amount (2 decimal places, non-negative validation)
  - Native date picker
  - Optional note text input
  - Submit button with native browser validation
- Built transaction list table with standard HTML table tags
- All elements and attributes follow standard English naming conventions
- Built static login page with standard form structure:
  - Username text input with semantic label binding
  - Password input with hidden character display
  - Native form submit button
  - Page navigation to transaction form after submission

## Tech Stack
### Frontend
- HTML5: semantic page structure, form controls, data table presentation

### Planned Tech Stack
- CSS3: responsive styling and UI optimization
- Vanilla JavaScript: client-side interaction logic
- Python Flask: backend REST API and business logic
- Relational Database: persistent data storage

## Project Structure
expense-tracker-web/
├── templates/
│   └── expense-form.html   # Static transaction creation page
└── README.md
└── login.html          # Static login page



## How to Run Locally
1. Clone the repository to your local machine
2. Open `templates/login.html` or `templates/expense-form.html` directly in any web browser


## Future Roadmap
- Backend integration with Flask to handle form submission and dynamic data rendering
- UI styling and responsive design with CSS
- Database integration to support full CRUD operations for transactions
- Feature expansion: statistics, filters and reporting functions
