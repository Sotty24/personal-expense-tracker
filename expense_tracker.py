import json
import os

if os.path.exists("expenses.json"):
    with open("expenses.json", "r") as file:
              expenses = json.load(file)
else:
    expenses = []

while True:
    print("==============================")
    print("PERSONAL EXPENSE TRACKER")
    print("==============================")
    print("1. Add an Expense")
    print("2. View Expenses")
    print("3. View Total Spent")
    print("4. Delete an Expense")
    print("5. Exit")

    choice = input("Please choose an option: ")

    if choice == "1":
        print("You have chosen: Add an Expense")
        expense = input("What did you spend your money on? ")

        try:
            amount = float(input("How much did you spend? "))
        except ValueError:
            print("That was not a valid number!")
            continue

        expenses.append((expense, amount))

        with open("expenses.json", "w") as file:
            json.dump(expenses, file)
        print("Expense added!")
        print("Item:", expense)
        print("Amount: £", amount)

    elif choice == "2":
        print("You have chosen: View Expenses")
        if len(expenses) == 0:
            print("No expenses have been added yet.")
        else:
            for number, (item, amount) in enumerate(expenses, start=1):
                print(number, "Item:", item)
                print("Amount: £", amount)

    elif choice == "3":
        print("You have chosen: View Total Spent")
        if len(expenses) == 0:
            print("The list is empty")
        else:
            total = 0
            for item, amount in expenses:
                total = total + amount
            print("Total spent: £", total)

    elif choice == "4":
        print("You have chosen: Delete an expense")
        if len(expenses) == 0:
            print("There are no expenses to delete")
        else:
            for number, (item, amount) in enumerate(expenses, start=1):
                print(number, "Item:", item)
                print("Amount: £", amount)

            delete_number = int(input("Enter the number of the expense you want to delete: "))

            if 1 <= delete_number <= len(expenses):
                deleted_expense = expenses.pop(delete_number - 1)

                with open("expenses.json", "w") as file:
                    json.dump(expenses, file)

                print(deleted_expense[0], "has been deleted!")
            else:
                print("Invalid expense number.")

    elif choice == "5":
        print("You have chosen: Exit")
        break

    else:
        print("Invalid choice. Please choose between 1, 2, 3, 4 or 5.")
