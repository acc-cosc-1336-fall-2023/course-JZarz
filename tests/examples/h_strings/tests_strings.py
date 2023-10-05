import unittest

from src.examples.h_strings.strings import concat_strings, search_str, slice_string, slice_w_step_value, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_concat_strings(self):
        self.assertEqual(concat_strings('abc', 'def'),'abcdef')
        self.assertEqual("abc"+"def", "abcdef")

    def test_slice_strings(self):
        name = "Patty Lynn Smith"
        self.assertEqual(slice_string("patty Lynn Smith"), "Lynn")
        self.assertEqual(name[11:], "Smith")

    def test_slice_w_step_value(self):

        letters = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(slice_w_step_value(letters[5:10]), "fhj")

    def test_compare_strings(self):
        str1 = 'c' #89
        str2 = 'p' #119
        #compare numerical letter check ascii
        self.assertEqual(str1 < str2, True)
        self.assertEqual(str1 > str2, False)


    def test_search_str(self):
        str1 = 'abc'
        str2 = 'abcdef'
        self.assertEqual(search_str(str1,str2), True)
        self.assertEqual(search_str('ef',str2), True)

    def test_is_string(self):
        str1 = '1200'
        self.assertEqual(str1.isdigit(), True)
        self.assertEqual("ab".isdigit(), False)

    def test_string_is_alpha(self):
        str1 = 'abc'
        self.assertEqual(str1.isalpha(), True)
        self.assertEqual("435".isalpha(),False)

    def test_string_is_upper(self):
        str1 ="LKJ"
        self.assertEqual(str1.isupper(),True)

    def test_string_to_lower(self):
        str1 = "aBCe"
        self.assertEqual(str1.lower(), "abce")

    def test_strip_string(self):
        str = 'eeabcdefgee'
        self.assertEqual(str.strip('e'), 'abcdefg')
        #strips letter from string ends only

    def test_lstrip_from_str(self):
        str = "aaxyza"
        self.assertEqual(str.lstrip('a'), 'xyza')

    #strips letter from str only in the beginning of str

    def test_r_strip_from_str(self):
        str = "abcdeaa"
        self.assertEqual(str.rstrip("a"), "abcde")
    #strips letter from str only in the end of str

    def test_replace_from_str(self):
        str = "eaebecefe"
        self.assertEqual(str.replace("e", ""), "abcf")
    #replace letters from str with ""

    def test_str_repetition_operator(self):
        str = 'w' * 5
        self.assertEqual(str,"wwwww")
    
    def test_split_str(self):
        str = "one two three four"
        str_list = str.split()
        self.assertEqual(str_list[0], "one")
        self.assertEqual(str_list[1], "two")
        self.assertEqual(str_list[2], "three")
        self.assertEqual(str_list[3], "four")

    def test_split_str_w_tab(self):
        str = "one\ttwo\tthree\tfour"
        str_list = str.split("\t")
        self.assertEqual(str_list[0], "one")