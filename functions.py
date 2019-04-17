def mainMenu():
    print("Please find below options available for user:")
    print("1. Display costs")
    print("2. Manage costs")
    print("3. Exit")

def selectMenu():
    while True:
        try:
            menu_select = int(input("Please select the option from menu by typing its refernce number (1-3) to proceed: "))
            if menu_select == 1:
                displayMenu()
                break
            elif menu_select == 2:
                manageCostsMenu()
                break
            elif menu_select == 3:
                exitMenu()
                break
            else:
                print("Please choose number 1,2 or 3")
                menu_select
        except ValueError:
            print("Invalid input, only digits are supported")


def displayMenu():
    print("DISPLAY MANU PLACEHOLDER")

def manageCostsMenu():
    print("MANAGE COSTS MENU PLACEHOLDER")

def exitMenu():
    print("Do you want to quit?")
    while True:
        try:
            quit_program = input("Y - Yes, N - No: ")
            if quit_program == "Y":
                break
        except ValueError:
            print('Supported options are "Y" or "N"')
    #want to quit Y/N