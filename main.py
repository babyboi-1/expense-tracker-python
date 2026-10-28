#Expense Tracker Application
#Built with Python,JSON,and SQlite
#Version control managed using git
print("NEW VERSION OF EXPENSE TRACKER IS RUNNING")
import json
from datetime import date, datetime
from database import add_expense_to_database
def display_menu():
    print("\n========EXPENSE TRACKER========")
    print("1.Add expenses.")
    print("2.View Expenses.")
    print("3.View Total Spending.")
    print("4.Exit.")
    print("5.Delete expenses.")
    print("6.Add expenses by category.")
    print("7.View spending by category")
    print("8.Check budget.")
    print("9.Set or change budget.")
    print("10.View spending by date.")
    print("11.Edit an expense.")
    print("12.Set or change category budgets.")
    print("13.Check category budgets.")
    print("14.Generate spending summary report")
    print("15.Add expense to SQlite!")
def load_expenses():
    try:
        with open ("expenses.json","r",encoding="utf-8")as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def load_budget():
    try:
        with open("budget.json","r",encoding="utf-8")as file:
            data=json.load(file)
            return data["budget"]
    except FileNotFoundError:
        return 1000.0
def save_budget(budget):
    with open("budget.json","w",encoding="utf-8")as file:
        json.dump({"budget":budget},file,indent=4)
def set_budget ():
    try:
        budget=float(input("Enter your new budget in KSh:"))
        if budget <= 0:
            print("Budget must be greater than zero.")
            return None
        save_budget(budget)
        print(f"Budget set to KSh{budget:.2f}")
        return budget
    except ValueError:
        print("Invalid amount.Please enter a number")
        return None
def save_expenses(expenses):
    with open("expenses.json","w",encoding="utf-8")as file:
        json.dump(expenses,file,indent=4)
def add_expense(expenses):
    description = input("Enter expense description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return
    try:
        amount = float(input("Enter amount in KSh: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    category = input("Enter category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return
    expense = {
        "description": description,
        "amount": amount,
        "category": category,
        "date":str(date.today())
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n========YOUR EXPENSES========")
    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['description']} | "
            f"KSh {expense['amount']:.2f} | "
            f"{expense['category']}"
            f"Date:{expense.get('date',"No date recorded")}"
        )
def edit_expense (expenses):
    if not expenses:
        print("No expenses available to edit.")
        return
    view_expenses(expenses)
    try:
        number=int(input("Enter the expense number to edit:"))
        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return
        expense=expenses[number-1]
        print("Press Enter to keep the existing value.")
        new_description=input(
           f"New description({expense['description']}):" 
        )       
        new_amount=input(
            f"New amount({expense['amount']}):"
        )
        new_category=input(
            f"New category({expense['category']}):"
        )
        if new_description.strip():
            expense["description"]=new_description.strip()
        if new_amount.strip():
            amount=float(new_amount)
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
            expense["amount"]=amount
        if new_category.strip():
            expense["category"]=new_category.strip()
        save_expenses(expenses)
        print("Expense updated successfully!")
    except ValueError:
        print("Invalid input:Enter a valid number for expense and amount")

def delete_expense(expenses):
    if not expenses:
        print("No expenses available to delete")
        return
    view_expenses(expenses)
    try:
        number=int(input("Enter expense number to delete:"))
        if number < 1 or number> len(expenses):
            print("Invalid expense number")
            return
    except ValueError:
        print("Please enter a valid whole number")
        return
    deleted_expense=expenses.pop(number-1)
    save_expenses(expenses)
    print("Deleted:", deleted_expense["description"])
    print("Amount: KSh", round(deleted_expense["amount"], 2))
def search_expenses_by_category(expenses):
    if not expenses:
        print("No expenses recorded yet!")
        return
    category=input("Enter category to search:").strip()
    if not category:
        print("Category cannot be empty")
        return
    matching_expenses=[]
    for expense in expenses:
        if expense["category"].lower()==category.lower():
            matching_expenses.append(expense) 
    if not matching_expenses:
        print(f"No expenses found in category '{category}'.")
        return
    print(f"\n ===========EXPENSES IN {category.upper()}=========")
    for number,expense in enumerate(matching_expenses,start=1):
        print(
            f"{number}. {expense['description']} |"
            f"Ksh.{expense['amount']:.2f} |"
            f"{expense['category']}"
        )
def view_spending_by_category(expenses):
    if not expenses:
        print("No expenses recorded yet")
        return
    category_totals={}
    for expense in expenses:
        category=expense["category"]
        amount=expense["amount"]
        if category in category_totals:
            category_totals[category]+=amount
        else:
            category_totals[category]=amount
    print("\n=========SPENDING BY CATEGORY=======")
    for category,total in category_totals.items():
        print(f"{category}:KSh{total:.2f}")
def valid_date(date_text):
    try:
        datetime.strptime(date_text,"%Y-%m-%d")
        return True
    except ValueError:
        return False  
def view_spending_by_date(expenses):
    if not expenses:
        print("No expenses recorded yet")
        return
    selected_date=input("Enter date(YYYY-MM-DD):")
    if not valid_date(selected_date):
        print("Invalid date use YYYY-MM-DD.")
        return
    daily_total=0
    found=False
    for expense in expenses:
        if expense.get("date")==selected_date:
            daily_total += expense["amount"]
            found=True
    if found :
        print(
            f"Total spending on {selected_date}:"
            f"Ksh{daily_total:.2f}"
            )           
    else:
        print(f"No expenses found for {selected_date}.")
def load_category_budgets():
    try:
        with open("category_budgets.json","r",encoding="utf=8")as file:
            return json.load(file)
    except FileNotFoundError:
        return{}
def save_category_budgets(category_budgets):
    with open("category_budgets.json","w",encoding="utf-8")as file:
        json.dump(category_budgets,file,indent=4)
def set_category_budget(category_budgets):
    category=input("Enter category:").strip()
    if not category:
        print("Category cannot be empty.")
        return
    try:
        budget=float(input("Enter budget in Ksh:"))
        if budget <= 0:
            print("Budget must be greater than zero!")
            return
        category_budgets[category]=budget
        save_category_budgets(category_budgets)
        print(f"Budget for {category}:Ksh{budget:.2f}")
    except ValueError:
        print("Invalid Amount.Please enter a number.")
def check_category_budgets(expenses,category_budgets):
    if not category_budgets:
        print("No category budgets set yet")
        return
    category_totals={}
    for expense in expenses:
        category=expense["category"]
        category_totals[category]=(
            category_totals.get(category,0)+expense["amount"]
        )
    for category,budget in category_budgets.items():
        spent=category_totals.get(category,0)
        remaining=budget-spent
        print(f"\nCategory:{category}")
        print(f"Budget:Ksh{spent:.2f}")
        print(f"Spent: Ksh{spent:.2f}")
        print(f"Remaining:Ksh{remaining:.2f}")
    if remaining < 0:
        print("WARNING:Category budget exceeded!")
    else:
        print("You are within this category's budget")
def check_budget(expenses,budget):
    total = sum(expense["amount"]for expense in expenses)
    print(f"Budget:KSh{budget:.2f}")
    print(f"Total spending:KSh{total:.2f}")
    print(f"Remaining budget:KSh{budget-total:.2f}")
    if total>budget:
        print("WARNING:You have exceeded yor budget!")
    elif total == budget:
        print("You have reached your budget limit")
    else:
        print("You are within the budget") 
def view_total_spending(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: KSh {total:.2f}")
def generate_spending_report(expenses,budget):
    print("\n===SPENDING SUMMARY REPORT=====")
    if not expenses:
        print("No expenses recorded yet.")
        return
    total_spending=0
    category_totals={}
    for expense in expenses:
        amount=expense["amount"]
        category=expense["category"]
        total_spending += amount
        category_totals[category]=(
            category_totals.get(category,0)+ amount
        ) 
    number_of_expenses=len(expenses)
    average_expenses=total_spending/number_of_expenses
    highest_expense=max(expenses,key=lambda expense:expense["amount"])
    highest_category=max(category_totals,key=category_totals.get)
    print(f"Number of expenses:{number_of_expenses}")
    print(f"Total spending:Ksh{total_spending:.2f}")
    print(f"Average expense:Ksh{average_expenses:.2f}")
    print(
        f"Highest expense:{highest_expense['description']}"
        f"(Ksh{highest_expense['amount']:.2f})"
    )
    print(
        f"Highest spending category:{highest_category}"
        f"Ksh{category_totals[highest_category]:.2f}"
    )
    print(f"Overall budget:Ksh{budget:.2f}")
    print(f"Budget remaining:Ksh{budget-total_spending:.2f}")
    if total_spending > budget:
        print("Status: OVER BUDGET")
    else:
        print("Status:WITHIN BUDGET")
    print("=====================================================")
def add_expense_sqlite():
    description=input("Enter expense description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return
    try:
        amount=float(input("Enter amount in KSh:"))
        if amount <=0 :
            print("Amount must be greater than zero")
            return
    except ValueError:
        print("Invalid amount.Please enter a number.")
        return
    category=input("Enter category:").strip()
    if not category:
        print("Category cannot be empty.")
        return
    expense_date=str(date.today())
    add_expense_to_database(
        description,
        amount,
        category,
        expense_date
    )
def main():
    category_budgets=load_category_budgets()
    expenses = load_expenses()
    budget=load_budget()
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total_spending(expenses)
        elif choice == "4":
            print("Goodbye!")
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            search_expenses_by_category(expenses)
        elif choice == "7":
            view_spending_by_category(expenses)
        elif choice == "8":
            check_budget(expenses,budget)
        elif choice == "9":
            new_budget = set_budget()
            if new_budget is not None:
               budget = new_budget
        elif choice == "10":
            view_spending_by_date(expenses)
        elif choice == "11":
            edit_expense(expenses)
        elif choice == "12":
            set_category_budget(category_budgets)
        elif choice ==  "13":
            check_category_budgets(expenses,category_budgets)
        elif choice == "14":
            generate_spending_report(expenses,budget)
        elif choice == "15":
            add_expense_sqlite()
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()