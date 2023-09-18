import unittest

from src.examples.d_repetition.repetition import sum_of_square, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_sum_of_squares(self):
        self.assertEqual(sum_of_square(3), 14)
        self.assertEqual(sum_of_square(4), 30)
        self.assertEqual(sum_of_square(5), 55)
        self.assertEqual(sum_of_square(-1), 0)


