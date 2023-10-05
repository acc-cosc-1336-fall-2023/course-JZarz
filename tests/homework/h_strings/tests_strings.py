import unittest
from src.homework.h_strings.strings import get_dna_complement, get_hamming_distance

class test_config(unittest.TestCase):
    def test_get_hamming_distance(self):
        self.assertEqual(get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"),7)


    def test_get_dna_complement(self):
       self.assertEqual(get_dna_complement("AAAACCCGGT"), "ACCGGGTTTT")