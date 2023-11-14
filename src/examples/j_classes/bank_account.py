import random
class BankAccount:
    __balance = 0 #keeps it private from other classes

    def __init__(self, balance): #constructio -- initialze class data/var
        
        if(balance>= 0 ):
            self.__balance = balance
        else:
            self.__get_balance_from_db()#this is a private function and not accepted in other classes
        
    def get_balance(self):#public other classes can access
        return self.__balance
    
    def deposit(self, amount):

        if (amount > 0):
            self.__balance += amount

    def withdraw(self, amount):
        if (amount > 0 and amount <= self.__balance):
            self.__balance -= amount

    def __get_balance_from_db(self):
            self.__balance = random.randint(0, 10000)
