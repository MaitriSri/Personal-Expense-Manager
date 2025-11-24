class ExpenseManager:
    def __init__(self):
        self.expenses = []



        
        cat = input("Category: ")
        desc = input("Description: ")

        self.expenses.append({
            "amount": amount,
            "category": cat,
            "description": desc
        })
        print("Expense added!\n")


    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses found.\n")
            return
        
        print("\n--- All Expenses ---")
        i = 1
        for e in self.expenses:
            print(i, e["amount"], e["category"], e["description"])
            i += 1
        print("")


    def summary(self):
        if len(self.expenses) == 0:
            print("Nothing to summarize.\n")
            return

        total = 0
        cat_sum = {}

        for e in self.expenses:
            total += e["amount"]
            c = e["category"]
            if c in cat_sum:
                cat_sum[c] += e["amount"]
            else:
                cat_sum[c] = e["amount"]

        print("\nTotal Spent:", total)
        print("--- Category Wise ---")
        for c,a in cat_sum.items():
            print(c, ":", a)
        print("")


def main():
    m = ExpenseManager()

    while True:
        print("=== Expense Manager ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary")
        print("4. Exit")

        ch = input("Choose: ")

        if ch == "1":
            m.add_expense()
        elif ch == "2":
            m.view_expenses()
        elif ch == "3":
            m.summary()
        elif ch == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice\n")


if __name__ == "__main__":
    main()
