class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount!")
            return
        
        category = input("Enter category (Food, Travel, Shopping etc.): ")
        description = input("Enter description: ")

        self.expenses.append({
            "amount": amount,
            "category": category,
            "description": description
        })
        print("Expense added successfully!\n")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.\n")
            return

        print("\n--- All Expenses ---")
        for i, exp in enumerate(self.expenses, 1):
            print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['description']}")
        print()

    def summary(self):
        if not self.expenses:
            print("No expenses to summarize.\n")
            return

        total = sum(e["amount"] for e in self.expenses)
        print(f"\nTotal Expense: ₹{total}")

        category_totals = {}
        for e in self.expenses:
            category_totals[e["category"]] = category_totals.get(e["category"], 0) + e["amount"]

        print("\n--- Category Summary ---")
        for cat, amt in category_totals.items():
            print(f"{cat}: ₹{amt}")
        print()


def main():
    manager = ExpenseManager()

    while True:
        print("===== Expense Manager =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_expense()
        elif choice == "2":
            manager.view_expenses()
        elif choice == "3":
            manager.summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()

