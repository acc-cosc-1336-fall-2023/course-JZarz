import bank_account, atm, menu

'''
account = bank_account.BankAccount(50)
my_atm = atm.ATM(account)
#print(account.get_balance())
my_atm.make_dep()
my_atm.display_balance()

my_atm.make_withdraw()
my_atm.display_balance()


amount = int(input("enter deposit amount: "))
account.deposit(amount)

print(account.get_balance())

amount = int(input("enter deposit amount: "))
account.withdraw(amount)
print(account.get_balance())
'''

account = bank_account.BankAccount(50)
my_atm = atm.ATM(account)

menu.run_menu(my_atm)