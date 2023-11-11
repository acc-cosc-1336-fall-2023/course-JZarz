import random
class Die:
    def __init__(self):
        self.__roll_value = None
    def roll(self):
        self.__roll_value = random.randint(1, 6)
    def get_roll_value(self):
        return self.__roll_value
    def __str__(self):
        print(f'The value you rolled is {self.__roll_value}')

def display_menu(Die):
        choice = input('select Choice \n 1. Roll Dice\n 2. Exit: ')
        if choice == '1':
            Die.roll()
            Die.__str__()
            cont(Die)
        elif choice == '2':
            print('Exiting')
        else:
            print('Invalid Entry')
def cont(Die):
        answer = input('Would you like to continue? Select Y or N: ')
        if answer.upper() == 'Y':
            display_menu(Die)
        elif answer.upper() == 'N':
            print('Exiting')
        else:
            print('Invalid Entry')