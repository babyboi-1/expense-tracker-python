import json
import sqlite3
def migrate_expenses():
    try:
        with open("expenses.json","r",encoding="utf-8")as file:
            expenses=json.load(file)
    except FileNotFoundError:
        print("expenses.json was not found.")
        return
    except json.JSONDecodeError:
        print("expenses.json contains invalid JSON.")
        return
    if not isinstance(expenses,list):
        print("Expected a list of expenses in expenses.json.")
        return
    connection=sqlite3.connect("expenses.db")
    cursor=connection.cursor()
    cursor.execute("""
       CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
       )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS migration_history(
            name TEXT PRIMARY KEY
        )
    """)
    migration_name="expenses_json_v1"
    cursor.execute(
        "SELECT name FROM migration_history WHERE name=?",
        (migration_name,)
    )
    if cursor.fetchone()is not None:
        print("JSON expenses have already been migrated.")
        connection.close()
        return
    for expense in expenses:
        description=expense["description"]
        amount=expense["amount"]
        category=expense["category"]
        expense_date=expense.get("date","Unknown")
        cursor.execute("""
            INSERT INTO expenses(description,amount,category,date)
            VALUES(?,?,?,?)
        """,(description,amount,category,expense_date))
        cursor.execute(
            "INSERT INTO migration_history(name)VALUES(?)",
            (migration_name,)
        )
        connection.commit()
        connection.close()
        print(f"Successfully migrated {len(expenses)}expenses!")
if __name__ == "__main__":
    migrate_expenses()