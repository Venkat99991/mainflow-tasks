import json

def get_income():
    while True:
        try:
            income = float(input("Enter your monthly income: "))
            if income < 0:
                raise ValueError("Income cannot be negative.")
            return income
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def get_expenses():
    expenses = {}
    print("Enter your expenses (type 'done' when finished):")
    while True:
        category = input("Enter expense category: ").strip()
        if category.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter amount for {category}: "))
            if amount < 0:
                raise ValueError("Expense cannot be negative.")
            expenses[category] = amount
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    return expenses

def analyze_expenses(income, expenses):
    total_expenses = sum(expenses.values())
    print("\n--- Expense Analysis ---")
    if total_expenses > income:
        print("Warning: Your expenses exceed your income!")
    print(f"Total Expenses: {total_expenses}")
    print(f"Remaining Income: {income - total_expenses}\n")

    print("--- Category Breakdown ---")
    for category, amount in expenses.items():
        percentage = (amount / income) * 100
        print(f"{category}: {percentage:.2f}% of income")

    if total_expenses > 0.8 * income:
        print("\nSuggestion: Try to limit your expenses to 80% of your income.")
    elif total_expenses < 0.5 * income:
        print("\nGood job! You're saving a significant portion of your income.")

def save_data(income, expenses, filename="budget_data.json"):
    data = {"income": income, "expenses": expenses}
    try:
        with open(filename, "w") as file:
            json.dump(data, file)
        print("\nBudget data saved successfully.")
    except IOError as e:
        print(f"Error saving data: {e}")

def main():
    print("Welcome to the Personal Budget Advisor!")
    income = get_income()
    expenses = get_expenses()
    analyze_expenses(income, expenses)
    save_data(income, expenses)

if __name__ == "__main__":
    main()
