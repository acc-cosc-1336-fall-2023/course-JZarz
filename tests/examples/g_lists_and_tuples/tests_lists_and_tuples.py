import unittest

from src.examples.g_lists_and_tuples.lists import get_list_total_for, get_list_total_while, list_ref_param, test_config
#from src.examples.g_lists_and_tuples.lists import list_tuples

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_list_total_while(self):
        list = [5, 10 ,20]
        self.assertEqual(get_list_total_while(list),35)

    def test_get_list_total_for(self):
        list = [5, 10 ,20]
        self.assertEqual(get_list_total_for(list),35)

    def test_get_ref_param(self):
        list = [5, 10, 20]
        list_ref_param(list)
        self.assertEqual(list, [0,10,20])
