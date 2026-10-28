# Python Expense Tracker

A command-line Expense Tracker application built with Python. This project helps users record expenses, monitor spending, organize transactions by category, and manage budgets.

## Features

- Add and view expenses
- Edit and delete expense records
- Search expenses by category
- Calculate total spending
- View spending by category and date
- Set an overall spending budget
- Set category-specific budgets
- Generate spending summary reports
- Store expenses using JSON
- Practice SQLite database operations

## Technologies Used

- **Python** — Application logic
- **JSON** — Local expense and budget storage
- **SQLite** — Database storage and SQL practice
- **Git** — Version control
- **GitHub** — Repository hosting

## Project Structure

```text
expense_tracker/
    main.py
    database.py
    migrate.py
    README.md
    .gitignore
```

- `main.py` — Main application and menu
- `database.py` — SQLite database functions
- `migrate.py` — Transfers existing JSON expenses to SQLite
- `.gitignore` — Excludes private data and generated files from Git

## Requirements

- Python 3 installed
- A terminal or Visual Studio Code

No third-party Python packages are required for the core project.

## How to Run

1. Download or clone this repository.
2. Open the project folder in a terminal.
3. Run:

```powershell
python main.py
```

4. Follow the menu instructions to manage expenses.

## Database

The project includes SQLite practice functions for inserting, viewing, updating, deleting, and summarizing expenses.

The original application still uses JSON for several features. SQLite integration is being developed incrementally.

## Privacy

Expense records, budget files, and local databases are excluded from Git using `.gitignore`.

Do not commit personal financial information or secret credentials.

## Future Improvements

- Complete SQLite integration
- Add monthly spending reports
- Add charts for spending analysis
- Export reports to CSV
- Improve error handling

## Author

Created as a hands-on Python learning project.