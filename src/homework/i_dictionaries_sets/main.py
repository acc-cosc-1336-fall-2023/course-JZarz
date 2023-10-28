import sets, dictionary

inventory = {}

def menu():
    choice = input(" 1. Add or update Inventory\n 2. Remove Inventory\n 3. Exit\n Choose option: ")
    options(choice)

def options(choice):
    
    if choice != '3':
        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        else:
            print('Invalid option')
    else:
        print('Program Will Exit')

def option1():
    number = int(input('how many items would you like to add and/ or revise? '))
    for i in range(0, number):
        
        widget_name = input('Name of item you want to add/revise: ')
        quantity = input('Quantity: ')
        dictionary.add_inventory(widget_name,quantity, inventory)
        i += 1
    
    print('Inventory:', inventory)
    cont()

def option2():
    widget_name = input('Name of item you want to remove: ')
    dictionary.remove_inventory(widget_name,inventory)
    print('Inventory:', inventory)
    cont()

def cont():
    answer = input('would you like to continue?\nY/N: ')

    if answer.upper() == 'Y':
        menu()
    elif answer.upper() == 'N':
        print('Final Inventory:', inventory)
        print('Program Exited')
    else:
        print('Invalid Option')
    

menu()
