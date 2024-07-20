import datetime

MAX_BUDGET = 1000.00


class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.date = datetime.datetime.now()


def add_expense(budget, expense):
    """
    Add an expense to the budget if it doesn't exceed the maximum.

    Args:
    budget (list): List of current expenses
    expense (Expense): Expense to be added

    Returns:
    bool: True if expense was added, False otherwise
    """
    total_spent = sum(e.amount for e in budget)
    if total_spent + expense.amount <= MAX_BUDGET:
        budget.append(expense)
        return True
    return False


def print_budget_report(budget):
    """Print a report of all expenses and total spent."""
    print("Budget Report:")
    for i, expense in enumerate(budget, 1):
        print(f"{i}. {expense.name}: ${expense.amount:.2f} "
              f"(on {expense.date.strftime('%Y-%m-%d')})")

    total_spent = sum(expense.amount for expense in budget)
    print(f"\nTotal Spent: ${total_spent:.2f}")
    print(f"Remaining Budget: ${MAX_BUDGET - total_spent:.2f}")


if __name__ == "__main__":
    my_budget = []

    # Adding some expenses
    expenses = [
        Expense("Groceries", 50.25),
        Expense("Gas", 30.00),
        Expense("Movie Night", 25.50),
        Expense("New Laptop", 899.99)
    ]

    for expense in expenses:
        if add_expense(my_budget, expense):
            print(f"Added: {expense.name}")
        else:
            print(f"Couldn't add {expense.name}: Exceeds budget")

    print("\n")
    print_budget_report(my_budget)