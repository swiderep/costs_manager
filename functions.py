import displayMenu
import manageCostsMenu

#this is a main menu poping up when the program starts
def mainMenu():
    print("Please find below options available for user:")
    print("1. Display costs")
    print("2. Manage costs")
    print("3. Exit")
    selectMenu()

#select sub-menu from main menu. Only digit inputs are valid, error handling for non-digit input
def selectMenu():
    while True:
        try:
            menu_select = int(input("Please select the option from menu by typing its refernce number (1-3) to proceed: "))
            if menu_select == 1:
                displayMenu.displayMenu()
                break
            elif menu_select == 2:
                manageCostsMenu.manageCostsMenu()
                break
            elif menu_select == 3:
                exitMenu()
                break
            else:
                print("Please choose number 1,2 or 3")
                menu_select
        except ValueError:
            print("Invalid input, only digits are supported")


#enter exit menu
def exitMenu():
    print("Do you want to quit?")
    while True:
        try:
            quit_program = input("Y - Yes, N - No: ")
            if quit_program == "Y":
                break
            elif quit_program == "N":
                mainMenu()
                break
            else:
                print('Supported options are "Y" or "N"')
        except ValueError:
            print('Supported options are "Y" or "N"')

