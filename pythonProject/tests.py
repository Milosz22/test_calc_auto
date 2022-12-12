import unittest
from main import *




class TestStringMethods(unittest.TestCase):

    def test_add(self):
        # given
        a = 2
        b = 3
        expected = 5
        # when
        result = wynik(a, b, '+')
        #then
        self.assertEqual(expected,result)

    def test_mult(self):
        # given
        a = 2
        b = 3
        expected = 6
        # when
        result = wynik(a, b, '*')
        #then
        self.assertEqual(wynik(a, b, '*'), 6)
    def test_sub(self):
        # given
        a = 2
        b = 3
        expected = -1
        # when
        result = wynik(a, b, '-')
        #then
        self.assertEqual(wynik(a, b, '-'), -1)
    def test_div(self):
        # given
        a = 2
        b = 3
        expected = 2/3
        # when
        result = wynik(a, b, '/')
        #then
        self.assertEqual(wynik(a, b, '/'), 2/3)
    def test_type_div(self):
        # given
        a = 2
        b = 3
        dzialanie ='/'
        expected_type=float
        # when
        result = wynik(a, b,dzialanie)
        #then
        self.assertEqual(type(result),expected_type)
    def test_type_add(self):
        # given
        a = 2
        b = 3
        dzialanie ='+'
        expected_type=int
        # when
        result = wynik(a, b,dzialanie)
        #then
        self.assertEqual(type(result),expected_type)
    def test_type_sub(self):
        # given
        a = 2
        b = 3
        dzialanie ='-'
        expected_type=int
        # when
        result = wynik(a, b,dzialanie)
        #then
        self.assertEqual(type(result),expected_type)
    def test_type_mult(self):
        # given
        a = 2
        b = 3
        dzialanie ='*'
        expected_type=int
        # when
        result = wynik(a, b,dzialanie)
        #then
        self.assertEqual(type(result),expected_type)


unittest.main()