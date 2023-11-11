import unittest

from src.homework.j_classes.class_a import Die

class Test_Config(unittest.TestCase):
    def test_get_roll_value(self):
        my_dice = Die()
        my_dice.roll()
        roll_value = my_dice.get_roll_value()
        self.assertTrue(roll_value, (1<= roll_value >=6))
        roll_value = my_dice.get_roll_value()
        self.assertTrue(roll_value, (1<= roll_value >=6))
        roll_value = my_dice.get_roll_value()
        self.assertTrue(roll_value, (1<= roll_value >=6))