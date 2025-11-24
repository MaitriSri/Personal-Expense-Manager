class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        print("\n--- Add Expense ---")
        try:
            amount = float(input("Amount: "))
        except:
            print("Invalid amount")
            return
        
        cat = input("Category: ")
        desc = input("Description: ")

        # storing single expense
        data = {
            "amount": amount,
            "category": cat,
            "description": desc
        }

        self.expenses.append(data)
        print("Expense added!")

    def view_expenses(self):
        print("Feature not finished yet.")

    def summary(self):
        print("Feature not finished yet.")


def main():
    manager = ExpenseManager()

    while True:
        print("\n=== Expense Manager ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Summary")
        print("4. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            manager.add_expense()
        elif ch == "2":
            manager.view_expenses()
        elif ch == "3":
            manager.summary()
        elif ch == "4":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
