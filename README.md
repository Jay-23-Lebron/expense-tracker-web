# Expense Tracker Web
A full-stack personal income & expense management web application, built as a portfolio project for IT career development.

## Current Progress
✅ **Phase 1 - Static HTML Foundation (Completed)**
- Built static transaction creation form with core fields:
  - Transaction type dropdown (Income / Expense)
  - Number input for amount with robust validation logic
  - Native date picker
  - Optional note text input
- Custom client-side JavaScript validation (replaces native browser validation)
  - Rejects empty input and whitespace-only values
  - Blocks non-numeric text and invalid number formats
  - Ensures transaction amount is strictly greater than 0
  - Auto-trims leading and trailing whitespace before validation
  - Triggers on both submit button click and Enter key press
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
