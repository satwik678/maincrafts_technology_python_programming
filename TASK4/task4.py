import csv
import os
from datetime import datetime

FILE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "expenses.csv"
)


def initialize_file():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Amount", "Category", "Date"])


def read_expenses():
    initialize_file()

    expenses = []

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                expenses.append({
                    "name": row["Name"],
                    "amount": float(row["Amount"]),
                    "category": row["Category"],
                    "date": row["Date"]
                })
            except (ValueError, KeyError, TypeError):
                continue

    return expenses


def get_valid_amount():
    while True:
        amount_input = input("Enter amount (₹): ").strip()

        if not amount_input:
            print("Amount cannot be empty.")
            continue

        try:
            amount = float(amount_input)

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Invalid amount. Please enter numbers only.")


def get_valid_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()

        if not date:
            print("Date cannot be empty.")
            continue

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date

        except ValueError:
            print("Invalid date. Please enter a valid date in YYYY-MM-DD format.")
            print("Example: 2026-08-20")


def get_valid_month():
    while True:
        month = input("Enter month (YYYY-MM): ").strip()

        if not month:
            print("Month cannot be empty.")
            continue

        try:
            datetime.strptime(month, "%Y-%m")
            return month

        except ValueError:
            print("Invalid month. Please enter the month in YYYY-MM format.")
            print("Example: 2026-08")


def add_expense():
    print("\n" + "=" * 60)
    print("                 ADD EXPENSE")
    print("=" * 60)

    name = input("Enter expense name: ").strip()

    if not name:
        print("Expense name cannot be empty.")
        return

    amount = get_valid_amount()

    while True:
        category = input("Enter category: ").strip().title()

        if category:
            break

        print("Category cannot be empty.")

    date = get_valid_date()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            name,
            f"{amount:.2f}",
            category,
            date
        ])

    print("\n✓ Expense added successfully!")
    print(f"Name     : {name}")
    print(f"Amount   : ₹{amount:.2f}")
    print(f"Category : {category}")
    print(f"Date     : {date}")


def view_expenses():
    expenses = read_expenses()

    print("\n" + "=" * 75)
    print("                         VIEW EXPENSES")
    print("=" * 75)

    if not expenses:
        print("No expenses found.")
        return

    print(
        f"{'No.':<5}"
        f"{'Name':<20}"
        f"{'Amount':>12}"
        f"{'Category':<15}"
        f"{'Date':<12}"
    )

    print("-" * 75)

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index:<5}"
            f"{expense['name'][:18]:<20}"
            f"₹{expense['amount']:>10.2f}"
            f"{expense['category'][:14]:<15}"
            f"{expense['date']:<12}"
        )

    print("-" * 75)

    total = sum(expense["amount"] for expense in expenses)

    print(f"Number of expenses : {len(expenses)}")
    print(f"Total spending     : ₹{total:,.2f}")


def search_by_category():
    expenses = read_expenses()

    print("\n" + "=" * 60)
    print("                   SEARCH BY CATEGORY")
    print("=" * 60)

    while True:
        category = input("Enter category: ").strip().lower()

        if category:
            break

        print("Category cannot be empty.")

    matching_expenses = [
        expense
        for expense in expenses
        if expense["category"].lower() == category
    ]

    if not matching_expenses:
        print(f"\nNo expenses found for category '{category.title()}'.")
        return

    print(f"\nExpenses in category: {category.title()}")
    print("-" * 60)

    total = 0

    for expense in matching_expenses:
        print(
            f"{expense['date']} | "
            f"{expense['name']:<20} | "
            f"₹{expense['amount']:,.2f}"
        )

        total += expense["amount"]

    print("-" * 60)
    print(f"Category total: ₹{total:,.2f}")


def monthly_total():
    expenses = read_expenses()

    print("\n" + "=" * 60)
    print("                    MONTHLY TOTAL")
    print("=" * 60)

    month = get_valid_month()

    matching_expenses = [
        expense
        for expense in expenses
        if expense["date"].startswith(month)
    ]

    if not matching_expenses:
        print(f"\nNo expenses found for {month}.")
        return

    total = sum(
        expense["amount"]
        for expense in matching_expenses
    )

    print(f"\nExpenses for {month}")
    print("-" * 60)

    for expense in matching_expenses:
        print(
            f"{expense['date']} | "
            f"{expense['name']:<20} | "
            f"₹{expense['amount']:,.2f}"
        )

    print("-" * 60)
    print(f"Monthly total: ₹{total:,.2f}")


def show_menu():
    print("\n")
    print("=" * 60)
    print("              EXPENSE TRACKER 2.0")
    print("                 TASK 4 CLI")
    print("=" * 60)

    print("\nMAIN MENU")
    print("-" * 60)
    print("[1] Add Expense")
    print("[2] View Expenses")
    print("[3] Search by Category")
    print("[4] Monthly Total")
    print("[5] Exit")
    print("-" * 60)


def main():
    initialize_file()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_by_category()

        elif choice == "4":
            monthly_total()

        elif choice == "5":
            print("\nThank you for using Expense Tracker 2.0!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select an option from 1 to 5.")

        if choice != "5":
            input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    main()