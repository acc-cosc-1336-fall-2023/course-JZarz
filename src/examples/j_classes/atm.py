class ATM:
    #__bank_account = None

    def __init__(self, bank_account):
        self.__bank_account = bank_account

    def make_dep(self):
        amount = int(input('enter dep amount: '))
        self.__bank_account.deposit(amount)

    def make_withdraw(self):
        amount= int(input('enter withdraw amount: '))
        self.__bank_account.withdraw(amount)

    def display_balance(self):
        print(self.__bank_account.get_balance())