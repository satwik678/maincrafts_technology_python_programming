import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "expenses.csv")


def add_expense():
    name = input("Enter expense name: ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount])

    print("Expense added successfully.\n")


def view_expenses():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("No expenses found.\n")
        return

    print("\nExpense Name\tAmount")
    print("-" * 25)

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]}\t\t{row[1]}")

    print()


def total_expense():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("No expenses found.\n")
        return

    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            total += float(row[1])

    print(f"\nTotal Expense = ₹{total}\n")


def main():
    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            print("Thank you for using Expense Tracker.")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()