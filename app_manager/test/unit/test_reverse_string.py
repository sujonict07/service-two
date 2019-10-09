import unittest
from ....app_manager.utils import string_reverser


class TestBasic(unittest.TestCase):

    def setUp(self):
        self.input_string = "iPay"
        self.reverse_string = self.input_string[::-1]

    def test_reverse_string(self):
        reverse_string = string_reverser(self.input_string)
        self.assertEqual(self.reverse_string, reverse_string)
