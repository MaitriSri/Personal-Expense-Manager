class ExpenseManager:
    def __init__(self):
        self.expenses = []


    def add_expense(self):
        # will complete next
        print("Add expense feature coming soon.")


    def view_expenses(self):
        print("View expenses feature coming soon.")


    def summary(self):
        print("Summary feature coming soon.")


def main():
    manager = ExpenseManager()

    while True:
        print("\n=== Expense Manager ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_expense()
        elif choice == "2":
            manager.view_expenses()
        elif choice == "3":
            manager.summary()
        elif choice == "4":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
