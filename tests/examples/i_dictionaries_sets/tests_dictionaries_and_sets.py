import unittest

from src.examples.i_dictionaries_sets.dictionaries import is_key_in_dict, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_is_key_in_dict(self):
        phonebook = {'chris': '555-1111', 'katie':'555-2222', 'joanna': '555-3333'}

        self.assertEqual(is_key_in_dict("chris",phonebook), True)
        self.assertEqual(is_key_in_dict("cris", phonebook), False)

