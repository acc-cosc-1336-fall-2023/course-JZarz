import unittest

from src.examples.i_dictionaries_sets.dictionaries import add_friend_phonebook, delete_friend_phonebook, is_key_in_dict, test_config, update_friend_phonebook

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_is_key_in_dict(self):
        phonebook = {'chris': '555-1111', 'katie':'555-2222', 'joanna': '555-3333'}

        self.assertEqual(is_key_in_dict("chris",phonebook), True)
        self.assertEqual(is_key_in_dict("cris", phonebook), False)

    def test_add_friend(self):
        phonebook = {}
        add_friend_phonebook('chris', '555-5555', phonebook)
        self.assertEqual(phonebook,{'chris':'555-5555'})

    def test_update_friend_phonebook(self):
        phonebook = {'chris: 555-5555'}
        update_friend_phonebook('chris', '555-1111', phonebook)
        self.assertEqual(phonebook,{'chris': '555-1111'})

    def test_delete_friend_phonebook(self):
        phonebook = {'chris': '555-5555', 'katie': '555-1111', 'kyle': '555-2222'}
        delete_friend_phonebook('chris', phonebook)
        self.assertEqual(phonebook,{'katie': '555-1111', 'kyle': '555-2222'})

    def test_set_union(self):
        set1 = ([1,2,3,4])
        set2 = ([3,4,5,6])

        self.assertEqual(set1.union(set2),([1,2,3,4,5,6]))

    def test_set_difference(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])
        self.assertEqual(set2),set1([1,2])

    def test_set_symmetric_difference(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])

        self.assertequal(set1.symmetric_difference(set2), set([1,2,4,5]))