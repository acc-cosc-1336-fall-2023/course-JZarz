def display_menu():
    print('COSC Bank')
    print('1 Dep')
    print('2 Withdraw')
    print('3 Display Balance')
    print('4 Exit')

def run_menu(atm):
    menu_choice = 0
    while (menu_choice != 4):
        display_menu()
        menu_choice = input('enter choice: ')
        handle_menu(menu_choice, atm)

def handle_menu(menu_choice, atm):

    if (menu_choice == '1'):
        atm.make_dep()
    elif(menu_choice =='2'):
        atm.make_withdraw()
    elif(menu_choice == '3'):
        atm.display_balance()
    elif(menu_choice == '4'):
        print('exiting ')
    else:
        print('invalid choice')