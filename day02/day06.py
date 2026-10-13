import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    """Load expenses from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read expense file. Starting with an empty list.")
        return []


def save_expenses(expenses):
    """Save expenses to the JSON file."""
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)
    except OSError:
        print("Error: Could not save expenses.")


def get_amount():
    """Get and validate the expense amount."""
    while True:
        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount

        except ValueError:
            print("Invalid amount. Please enter a number.")


def get_category():
    """Get and validate the expense category."""
    while True:
        category = input("Enter category: ").strip()

        if category:
            return category

        print("Category cannot be empty.")


def get_date():
    """Get and validate the expense date."""
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD format.")


def add_expense(expenses):
    """Add a new expense."""
    print("\n--- Add Expense ---")

    amount = get_amount()
    category = get_category()
    date = get_date()

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses(expenses):
    """Display all saved expenses."""
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    print(f"{'No.':<5}{'Amount':<15}{'Category':<20}{'Date'}")
    print("-" * 55)

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index:<5}"
            f"₹{expense['amount']:<14.2f}"
            f"{expense['category']:<20}"
            f"{expense['date']}"
        )


def total_by_category(expenses):
    """Calculate and display total expenses for each category."""
    print("\n--- Total by Category ---")

    if not expenses:
        print("No expenses found.")
        return

    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    for category, total in totals.items():
        print(f"{category}: ₹{total:.2f}")


def show_menu():
    """Display the main menu."""
    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total by Category")
    print("4. Exit")
    print("=====================================")


def main():
    """Run the expense tracker program."""
    expenses = load_expenses()

    while True:
        show_menu()

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_by_category(expenses)

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()