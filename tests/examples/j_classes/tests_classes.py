import unittest

from src.examples.j_classes.bank_account import BankAccount

class Test_Config(unittest.TestCase):
    def test_bank_account_balance(self):
        account = BankAccount(0)
        self.assertEqual(account.get_balance(),0)

    def test_bankacc_dep(self):
        #steps to get balance would happen here
        account = BankAccount(50)

        account.deposit(100)
        self.assertEqual(account.get_balance(),150)

    def test_bank_account_deposit_neg_balance(self):
        account = BankAccount(50)
        account.deposit(-50)
        self.assertEqual(account.get_balance(),50)

    def test_bank_accounot_withdraw(self):
        account = BankAccount(50)
        account.withdraw(20)
        self.assertEqual(account.get_balance(), 30)

    def test_bank_acc_withdraw_neg(self):
        account = BankAccount(50)
        account.withdraw(-10)
        self.assertEqual(account.get_balance(), 50)

    def test_bank_acc_more_than_balance(self):
        account = BankAccount(50)
        account.withdraw(60)
        self.assertEqual(account.get_balance(), 50)

    def test_bank_acc_dep_and_withdraw(self):
        account = BankAccount(50)
        account.deposit(100)
        self.assertEqual(account.get_balance(), 150)

        account.withdraw(20)
        self.assertEqual(account.get_balance(), 130)

    def test_bank_acc_withdraw_and_dep(self):
        account = BankAccount(50)
        account.withdraw(20)
        self.assertEqual(account.get_balance(), 30)

        account.deposit(100)
        self.assertEqual(account.get_balance(), 130)

    def test_bank_account_get_balance_from_db(self):
        account = BankAccount(-1)
        self.assertGreaterEqual(account.get_balance(), 0)
        self.assertLessEqual(account.get_balance(), 10000)
        