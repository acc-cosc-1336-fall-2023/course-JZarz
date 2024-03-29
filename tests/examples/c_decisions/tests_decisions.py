import unittest

from src.examples.c_decisions.decisions import get_not_value, get_or_truth, is_consonant, is_even, is_odd, is_vowel, overtime, test_config
from src.examples.c_decisions.decisions import get_and_result
from src.examples.c_decisions.decisions import get_letter_grade

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())
    def test_and_truth_table(self):
        self.assertEqual(True, get_and_result(True, True))
        self.assertEqual(False, get_and_result(True, False))
        self.assertEqual(False, get_and_result(False, True))
        self.assertEqual(False, get_and_result(False, False))

    def test_or_truth(self):
        self.assertEqual(True, get_or_truth(True, True))
        self.assertEqual(True, get_or_truth(True, False))
        self.assertEqual(True, get_or_truth(False, True))

    def test_not_truth_table(self):
        self.assertEqual(True, get_not_value(False))
        self.assertEqual(False, get_not_value(True))

    def test_if_even(self):
        self.assertEqual(True, is_even(2))

    def test_if_odd(self):
        self.assertEqual(True,is_odd(1))
        self.assertEqual(True,is_odd(3))
        self.assertEqual(False,is_odd(2))
        self.assertEqual(False,is_odd(102))

    def test_if_vowel(self):
        self.assertEqual(True,is_vowel('a'))
        self.assertEqual(False,is_vowel('j'))

    def test_if_cons(self):
        self.assertEqual(False,is_consonant('a'))
        self.assertEqual(True,is_consonant('j'))

    def test_if_overtime(self):
        self.assertEqual(False, overtime(30))
        self.assertEqual(True, overtime(50))
    
    
def test_get_letter_grade(self):
    self.assertEqual(get_letter_grade(95),"A")
    self.assertEqual(get_letter_grade(100),"A")
    self.assertEqual(get_letter_grade(85),"B")
    self.assertEqual(get_letter_grade(80),"B")
    self.assertEqual(get_letter_grade(75),"C")
    self.assertEqual(get_letter_grade(70),"C")
    self.assertEqual(get_letter_grade(65),"D")
    self.assertEqual(get_letter_grade(50),"F")
    self.assertEqual(get_letter_grade(105),"Invalid Grade")
    