import unittest
from src.homework.i_dictionaries_sets.sets import get_p_distance, get_p_distance_matrix
from src.homework.i_dictionaries_sets.dictionary import add_inventory, difference_and_add, play_both_sports, play_sports_union, plays_1st_sport, plays_2nd_sport, plays_one_sport, remove_inventory

class test_config(unittest.TestCase):
    '''def test_get_p_distance(self):
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
        self.assertTrue(len(inventory) == 1, True)'''

    def test_play_both_sports(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(play_both_sports(basketball,baseball) , set(['Carmen', 'Alicia']))

    def test_plays_one_sport(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(plays_one_sport(basketball,baseball) , set(['Jodi', 'Aida','Eva', 'Sarah']))
    
    def test_play_sports_union(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(play_sports_union(baseball,basketball), set(['Jodi', 'Carmen', 'Aida', 'Alicia', 'Eva', 'Sarah']))
        
    def test_play_1st_sports_only(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(plays_1st_sport(baseball,basketball), set(['Jodi', 'Aida']))

    def test_play_2nd_sports_only(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(plays_2nd_sport(baseball,basketball), set(['Eva', 'Sarah']))

    def test_difference_and_add(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(difference_and_add(baseball,basketball), (set(['Jodi', 'Aida']),set(['Eva', 'Sarah'])))