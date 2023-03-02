def budget_tracker():
    # Initialize the budget
    budget = 0

    # A dictionary to keep track of expenses
    expenses = {}

    # Main loop to track the budget
    while True:
        print("Enter 1 to add income")
        print("Enter 2 to add expense")
        print("Enter 3 to view current budget")
        print("Enter 4 to exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            income = int(input("Enter the amount of income: "))
            budget += income
            print("Income added successfully!")
        elif choice == 2:
            expense_name = input("Enter the name of the expense: ")
            expense_amount = int(input("Enter the amount of the expense: "))
            budget -= expense_amount
            expenses[expense_name] = expense_amount
            print("Expense added successfully!")
        elif choice == 3:
            print("Current budget: ", budget)
            print("Current expenses: ", expenses)
        elif choice == 4:
            print("Exiting budget tracker...")
            break
        else:
            print("Invalid choice. Try again.")

# Call the budget_tracker function to start the program
budget_tracker()
