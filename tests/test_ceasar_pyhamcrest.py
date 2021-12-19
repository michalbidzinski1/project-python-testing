import unittest
from hamcrest import *
from src.sample.Ceasar import Ceasar
class TestCeasar(unittest.TestCase):
    def setUp(self):
        self.temp = Ceasar()
    def test_ceasar_letter(self):
        assert_that(self.temp.encrypt('a'), equal_to('d'))
    def test_ceasar_word(self):
        assert_that(self.temp.encrypt('VENI'), equal_to('YHQL'))
    def test_ceasar_last_3_letters(self):
        assert_that(self.temp.encrypt('XYZ'), equal_to('UVW'))
