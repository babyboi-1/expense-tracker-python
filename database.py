import sqlite3
connection=sqlite3.connect("expenses.db")
cursor=connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    amount REAL NOT  NULL,
    category TEXT NOT NULL,
    date TEXT NOT NULL
)
""")
connection.commit()
print("Expenses table created successfully")
connection.close()


def add_expense_to_database(description,amount,category,expense_date):
    connection=sqlite3.connect("expenses.db")
    cursor=connection.cursor()
    cursor.execute("""
         INSERT INTO expenses(description,amount,category,date)
         VALUES (?,?,?,?)
    """,(description,amount,category,expense_date))
    connection.commit()
    connection.close()
    print("Expense saved to database successfully!")

def view_database_expense():
    connection=sqlite3.connect("expenses.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses=cursor.fetchall()
    connection.close()
    for expense in expenses:
        print(expense)
def update_expense_amount(expense_id,new_amount):
    if new_amount <=0 :
        print("Amount must be greater than zero!")
        return
    connection=sqlite3.connect("expenses.db")
    cursor=connection.cursor()
    cursor.execute("""
        UPDATE expenses
        SET amount=?
        WHERE id=?
    """,(new_amount,expense_id))
    connection.commit()
    if cursor.rowcount >0:
        print("Expense updated successfully!")
    else:
        print("Expense ID not found.")
    connection.close()
def delete_expense_from_database(expense_id):
    connection=sqlite3.connect("expenses.db")
    cursor=connection.cursor()
    cursor.execute("""
         DELETE FROM expenses
         WHERE id = ?
    """,(expense_id,))
    connection.commit()
    if cursor.rowcount >0 :
        print("Expense deleted successfully!")
    else:
        print("Expense ID not found")
    connection.close()
def search_expenses_by_category(category):
    connection=sqlite3.connect("expenses.db")
    cursor=connection.cursor()
    cursor.execute("""
        SELECT * FROM expenses
        WHERE LOWER(category)= LOWER(?)
    """,(category,))
    expenses=cursor.fetchall()
    connection.close()
    if not expenses:
        print("No expenses found in this category: ")
        return
    for expense in expenses:
        print(expense)
def calculate_total_spending():
    connection=sqlite3.connect("expenses.db")
    cursor=connection.cursor()
    cursor.execute("SELECT SUM(amount)FROM expenses")
    result=cursor.fetchone()
    connection.close()
    total=result[0] if result[0]is not None else()
    print(f"Total spending:KSh{total:.2f}")
def calculate_spending_by_category():
    connection=sqlite3.connect("expenses.db")
    cursor=connection.cursor()
    cursor.execute("""
        SELECT category,SUM(amount)
        FROM expenses
        GROUP BY category
    """)
    results=cursor.fetchall()
    connection.close()
    if not results:
        print("No expenses recorded yet")
        return
    print("\n================SPENDING BY CATEGORY========================")
    for category,total in results:
        print(f"{category}:Ksh{total:.2f}")
if __name__=="__main__":
    view_database_expense()