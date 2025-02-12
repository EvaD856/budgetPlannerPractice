"""
    Your code goes below
"""
"""

"""
def addExpense(expenses):
    category = str(input("Enter the category: "))
    while True:
        amount = float(input("Enter the amount: $"))
        if amount >= 0:
            expenses[category] = expenses.get(category, 0) + amount
            print("Added",amount, "to",category,".")
            print("")
            break
        else:
            print("-Invalid expense amount, try again!-")

def viewSummary(getMonthlyIncome, expenses):
    print("")
    print("** Total income is $",getMonthlyIncome,"**")
    print("")
    print("Expenses:")
    print("")
    for category, amount in expenses.items():
        percentage = amount / getMonthlyIncome * 100
        print(f"{category}:{amount} ( {percentage:.2f} %") 
    print("")
    total = sum(expenses.values())
    print("Total Expenses: $", total)  
    remainder = getMonthlyIncome - total
    print("Remaining Budget: $", remainder)   
        
def getMonthlyIncome():
    monthlyIncome = float(input("Enter monthly income: $"))
    if monthlyIncome >= 0:
        return monthlyIncome
    else:
        print("Invalid input. Please enter a non-negative number.")


def displayMenu():
    print("--Menu--")
    print(" 1. Add an expense")
    print(" 2. View budget summary")
    print(" 3. Quit")
    print("")

def main():
    print("")
    print("Welcome to the Budget Planner and Expense Tracker!")
    print("")
    monthlyIncome = getMonthlyIncome()
    expenses = {}
    print("")
    while True:
        displayMenu()
        choice = int(input("Enter your choice (1-3):"))

        if choice == 1:
            addExpense(expenses)
        elif choice == 2:
            viewSummary(monthlyIncome, expenses)
        elif choice == 3:
            break
        else:
            print("Invalid choice, try again!")


"""
Code to start the application
"""
if __name__ == "__main__":
    main()