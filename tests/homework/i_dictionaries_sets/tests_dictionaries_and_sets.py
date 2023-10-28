import unittest
from src.homework.i_dictionaries_sets.sets import get_p_distance, get_p_distance_matrix
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory

class test_config(unittest.TestCase):
    def test_get_p_distance(self):
        self.assertEqual(get_p_distance(['T','T','T','C','C','A','T','T','T','A'],  ['G','A','T','T','C','A','T','T','T','C']), 4)

    def  test_get_p_distance_matrix(self):
        self.assertEqual(get_p_distance_matrix(
[['T','T','T','C','C','A','T','T','T','A'],['G','A','T','T','C','A','T','T','T','C'],['T','T','T','C','C','A','T','T','T','T'],['G','T','T','C','C','A','T','T','T','A']]), 
[[0.0, 0.4, 0.1, 0.1],[0.4, 0.0, 0.4, 0.3],[0.1, 0.4, 0.0, 0.2],[0.1, 0.3, 0.2, 0.0]])
        
    def test_add_inventory(self):
        inventory = {}
        add_inventory('widget1', '10', inventory)
        self.assertEqual(inventory,{'widget1':'10'})
        inventory = {'widget1':'35'}
        add_inventory('widget1','25', inventory)
        self.assertEqual(inventory,{'widget1':'25'})
        add_inventory('widget1','-10', inventory)
        self.assertEqual(inventory,{'widget1':'-10'})

    def test_remove_inventory(self):
        inventory = {'widget1': '20', 'widget2':'18'}
        remove_inventory('widget1', inventory)
        self.assertEqual(inventory,{'widget2':'18'})
        self.assertTrue(len(inventory) == 1, True)