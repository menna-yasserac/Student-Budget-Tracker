import json
import os

DATA_FILE = "users.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


users = load_data()

print("=== Student Budget Tracker ===")

username = input("Enter your name: ")

if username not in users:

    budget = float(input("Enter your monthly budget: "))

    users[username] = {
        "budget": budget,
        "expenses": {}
    }

    save_data(users)

    print("New account created successfully!")

else:
    print(f"Welcome back, {username}!")


while True:

    print("""
1. Add Expense
2. View Expenses
3. Show Total Spent
4. Show Remaining Budget
5. Exit
""")

    choice = int(input("Choose: "))

    if choice == 1:

        name = input("Expense name: ")
        category = input("Category: ")
        amount = float(input("Amount: "))

        # Create category if it doesn't exist
        if category not in users[username]["expenses"]:
            users[username]["expenses"][category] = {}

        # Add product and price
        users[username]["expenses"][category][name] = amount

        save_data(users)

        print("Expense added successfully!")

    elif choice == 2:

        expenses = users[username]["expenses"]

        if not expenses:
            print("No expenses found.")

        else:
            print("\n=== Your Expenses ===")

            for category, products in expenses.items():

                print(f"\n{category}:")

                for name, amount in products.items():
                    print(f"  {name}: {amount}")

    elif choice == 3:

        total = 0

        for products in users[username]["expenses"].values():
            total += sum(products.values())

        print(f"Total spent = {total}")

    elif choice == 4:

        total = 0

        for products in users[username]["expenses"].values():
            total += sum(products.values())

        remaining = users[username]["budget"] - total

        print(f"Remaining budget = {remaining}")

    elif choice == 5:

        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please choose from 1 to 5.")