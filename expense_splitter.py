expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add an expense")
    print("2. Show expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        description = input("What was the expense? ")

        try:
            amount = float(input("How much did it cost? "))

            if amount > 0:
                expenses.append([description, amount])
                print("Expense added.")
            else:
                print("The amount must be greater than zero.")
        except ValueError:
            print("Please enter a number.")

    elif choice == "2":
        if len(expenses) == 0:
            print("There are no expenses yet.")
        else:
            for expense in expenses:
                print(expense[0], "-", expense[1], "TL")

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense[1]

        print("Total:", total, "TL")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Please choose 1, 2, 3, or 4.")
