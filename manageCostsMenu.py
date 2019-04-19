import functions
import database

#enter cost management menu
def manageCostsMenu():
    print("Select action:")
    print("1. Add new cost")
    print("2. Edit existing cost")
    print("3. Remove existing cost")
    print("4. Back to main menu")
    manageCostChoice()

def manageCostChoice():
    while True:
        try:
            manageCostsMenuChoice = int(input("Select option from above: "))
            if manageCostsMenuChoice == 1:
                manageCostsAdd()
                break
            elif manageCostsMenuChoice == 2:
                manageCostsEdit()
                break
            elif manageCostsMenuChoice == 3:
                manageCostsRemove()
                break
            elif manageCostsMenuChoice == 4:
                functions.mainMenu()
                break
            else:
                print("Please select one of available options")
        except ValueError:
            print("Invalid input. Only digits are supported")

def manageCostsAdd():
    print("To add new costs please specify its name, amount and due date")
    # create a tuple or dictionary to add there new values which then will be inserted into table

def manageCostsEdit():
    print("Select a cost you want to edit")

def manageCostsRemove():
    print("Select a cost you want to remove")