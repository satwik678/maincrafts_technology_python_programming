import csv
import os
from datetime import datetime

FILE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "expenses.csv"
)

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def line(char="─", length=64):
    print(char * length)


def header():
    print(f"{CYAN}{BOLD}")
    print("╔" + "═" * 62 + "╗")
    print("║" + " " * 19 + "EXPENSE TRACKER 2.0" + " " * 22 + "║")
    print("║" + " " * 17 + "Personal Budget Manager" + " " * 22 + "║")
    print("╚" + "═" * 62 + "╝")
    print(RESET)


def add_expense():
    clear_screen()
    header()

    print(f"{GREEN}{BOLD}➜ ADD NEW EXPENSE{RESET}")
    line()

    name = input("  Expense name      : ").strip()

    if not name:
        print(f"{RED}  Expense name cannot be empty.{RESET}")
        input("\nPress Enter to continue...")
        return

    amount_input = input("  Amount (₹)        : ").strip()

    try:
        amount = float(amount_input)

        if amount <= 0:
            raise ValueError

    except ValueError:
        print(f"{RED}  Please enter a valid positive amount.{RESET}")
        input("\nPress Enter to continue...")
        return

    category = input("  Category          : ").strip().title()

    if not category:
        print(f"{RED}  Category cannot be empty.{RESET}")
        input("\nPress Enter to continue...")
        return

    date = input("  Date (YYYY-MM-DD) : ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")

    except ValueError:
        print(f"{RED}  Invalid date. Use YYYY-MM-DD.{RESET}")
        input("\nPress Enter to continue...")
        return

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writerow(["Name", "Amount", "Category", "Date"])

        writer.writerow([
            name,
            f"{amount:.2f}",
            category,
            date
        ])

    print()
    print(f"{GREEN}  ✓ Expense added successfully!{RESET}")
    print(f"  {name} | ₹{amount:.2f} | {category} | {date}")

    input("\nPress Enter to continue...")


def read_expenses():
    expenses = []

    if not os.path.exists(FILE_NAME):
        return expenses

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:

            if (
                row.get("Name")
                and row.get("Amount")
                and row.get("Category")
                and row.get("Date")
            ):

                try:
                    amount = float(row["Amount"])

                    expenses.append({
                        "name": row["Name"],
                        "amount": amount,
                        "category": row["Category"],
                        "date": row["Date"]
                    })

                except ValueError:
                    continue

    return expenses


def view_expenses():
    clear_screen()
    header()

    print(f"{BLUE}{BOLD}➜ ALL EXPENSES{RESET}")
    line()

    expenses = read_expenses()

    if not expenses:
        print(f"{YELLOW}  No expenses found.{RESET}")
        input("\nPress Enter to continue...")
        return

    print(
        f"{BOLD}"
        f"{'No.':<5}"
        f"{'Expense':<20}"
        f"{'Amount':>12}"
        f"{'Category':<15}"
        f"{'Date':<12}"
        f"{RESET}"
    )

    line()

    for index, expense in enumerate(expenses, start=1):

        print(
            f"{index:<5}"
            f"{expense['name'][:18]:<20}"
            f"₹{expense['amount']:>10.2f}"
            f"{expense['category'][:14]:<15}"
            f"{expense['date']:<12}"
        )

    line()

    print(f"{BOLD}Total Records: {len(expenses)}{RESET}")

    input("\nPress Enter to continue...")


def total_expense():
    clear_screen()
    header()

    print(f"{MAGENTA}{BOLD}➜ TOTAL EXPENSE{RESET}")
    line()

    expenses = read_expenses()

    if not expenses:
        print(f"{YELLOW}  No expenses found.{RESET}")
        input("\nPress Enter to continue...")
        return

    total = sum(
        expense["amount"]
        for expense in expenses
    )

    print()
    print(f"{BOLD}  Total money spent:{RESET}")
    print()
    print(f"{GREEN}{BOLD}                 ₹{total:,.2f}{RESET}")
    print()

    input("Press Enter to continue...")


def search_by_category():
    clear_screen()
    header()

    print(f"{YELLOW}{BOLD}➜ SEARCH BY CATEGORY{RESET}")
    line()

    category = input("  Enter category: ").strip().lower()

    if not category:
        print(f"{RED}  Category cannot be empty.{RESET}")
        input("\nPress Enter to continue...")
        return

    expenses = read_expenses()

    matches = [
        expense
        for expense in expenses
        if expense["category"].lower() == category
    ]

    print()

    if not matches:
        print(
            f"{RED}  No expenses found for "
            f"'{category}'.{RESET}"
        )

        input("\nPress Enter to continue...")
        return

    print(
        f"{GREEN}{BOLD}"
        f"  Results for: {category.title()}"
        f"{RESET}"
    )

    line()

    print(
        f"{BOLD}"
        f"{'Expense':<25}"
        f"{'Amount':>12}"
        f"{'Date':<15}"
        f"{RESET}"
    )

    line()

    category_total = 0

    for expense in matches:

        print(
            f"{expense['name'][:23]:<25}"
            f"₹{expense['amount']:>10.2f}"
            f"{expense['date']:<15}"
        )

        category_total += expense["amount"]

    line()

    print(
        f"{BOLD}"
        f"Category Total: ₹{category_total:,.2f}"
        f"{RESET}"
    )

    input("\nPress Enter to continue...")


def category_total():
    clear_screen()
    header()

    print(f"{MAGENTA}{BOLD}➜ SPENDING BY CATEGORY{RESET}")
    line()

    expenses = read_expenses()

    if not expenses:
        print(f"{YELLOW}  No expenses found.{RESET}")
        input("\nPress Enter to continue...")
        return

    totals = {}

    for expense in expenses:

        category = expense["category"]

        if category not in totals:
            totals[category] = 0

        totals[category] += expense["amount"]

    print(
        f"{BOLD}"
        f"{'Category':<25}"
        f"{'Total Spent':>15}"
        f"{RESET}"
    )

    line()

    for category, total in sorted(totals.items()):

        print(
            f"{category:<25}"
            f"₹{total:>13,.2f}"
        )

    line()

    grand_total = sum(totals.values())

    print(
        f"{BOLD}"
        f"{'Overall Total':<25}"
        f"₹{grand_total:>13,.2f}"
        f"{RESET}"
    )

    input("\nPress Enter to continue...")


def monthly_total():
    clear_screen()
    header()

    print(f"{BLUE}{BOLD}➜ MONTHLY SPENDING{RESET}")
    line()

    month = input("  Enter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")

    except ValueError:
        print(
            f"{RED}"
            f"  Invalid month. Use YYYY-MM."
            f"{RESET}"
        )

        input("\nPress Enter to continue...")
        return

    expenses = read_expenses()

    matches = [
        expense
        for expense in expenses
        if expense["date"].startswith(month)
    ]

    if not matches:

        print(
            f"\n{YELLOW}"
            f"  No expenses found for {month}."
            f"{RESET}"
        )

        input("\nPress Enter to continue...")
        return

    total = sum(
        expense["amount"]
        for expense in matches
    )

    print()
    print(
        f"{GREEN}{BOLD}"
        f"  MONTH: {month}"
        f"{RESET}"
    )

    line()

    print(f"  Number of expenses : {len(matches)}")
    print(f"  Total spending     : ₹{total:,.2f}")

    line()

    for expense in matches:

        print(
            f"  {expense['date']}  "
            f"{expense['name']:<20} "
            f"₹{expense['amount']:,.2f}"
        )

    input("\nPress Enter to continue...")


def dashboard():
    clear_screen()
    header()

    expenses = read_expenses()

    total = sum(
        expense["amount"]
        for expense in expenses
    )

    categories = {}

    for expense in expenses:

        category = expense["category"]

        categories[category] = (
            categories.get(category, 0)
            + expense["amount"]
        )

    print(f"{CYAN}{BOLD}➜ DASHBOARD{RESET}")
    line()

    print(f"  Total Expenses     : {len(expenses)}")
    print(f"  Total Spending     : ₹{total:,.2f}")
    print(f"  Categories Used    : {len(categories)}")

    line()

    if categories:

        print(f"{BOLD}  Top Categories{RESET}")
        print()

        sorted_categories = sorted(
            categories.items(),
            key=lambda item: item[1],
            reverse=True
        )

        for category, amount in sorted_categories[:5]:

            print(
                f"  • {category:<20}"
                f" ₹{amount:,.2f}"
            )

    else:

        print(
            f"{YELLOW}"
            f"  No spending data available yet."
            f"{RESET}"
        )

    print()

    input("Press Enter to continue...")


def main():

    while True:

        clear_screen()
        header()

        print(f"{BOLD}  MAIN MENU{RESET}")
        line()

        print("  [1]  Add Expense")
        print("  [2]  View All Expenses")
        print("  [3]  View Total Expense")
        print("  [4]  Search by Category")
        print("  [5]  Spending by Category")
        print("  [6]  Monthly Spending")
        print("  [7]  Dashboard")
        print("  [8]  Exit")

        line()

        choice = input("  Select an option: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            search_by_category()

        elif choice == "5":
            category_total()

        elif choice == "6":
            monthly_total()

        elif choice == "7":
            dashboard()

        elif choice == "8":

            clear_screen()

            print(
                f"\n{GREEN}{BOLD}"
                f"  Thank you for using Expense Tracker 2.0!"
                f"{RESET}\n"
            )

            break

        else:

            print(
                f"\n{RED}"
                f"  Invalid option. Please choose 1-8."
                f"{RESET}"
            )

            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()