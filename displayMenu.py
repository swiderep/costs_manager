import functions
# enter display menu
def displayMenu():
    print("Display by:")
    print("1. Due date")
    print("2. Amount")
    print("3. Back to main menu")
    displayChoice()

def displayChoice():
    while True:
        try:
            displayMenuChoice = int(input("Select option from above: "))
            if displayMenuChoice == 1:
                displayByDate()
                break
            elif displayMenuChoice == 2:
                displayByAmount()
                break
            elif displayMenuChoice == 3:
                functions.mainMenu()
                break
            else:
                print("Please select one of available options")
        except ValueError:
            print("Invalid input. Only digits are supported")

def displayByDate():
    print("Below table shows liabilities ordered by date")
    # here to select from liabilities table order by due date

def displayByAmount():
    print("Below table shows liabilities ordered by amount")
    # here to select from liabilities table order by amount
