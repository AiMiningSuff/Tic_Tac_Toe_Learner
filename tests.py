import unittest
from trainer import *

class TestAIMethods(unittest.TestCase):
    """
    Examples:

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    """
    
    def test_reflect_board(self):
        self.assertEqual( reflect_board([1, 0, 2, 1, 0]), [2, 0, 1, 2, 0] )

if __name__ == '__main__':
    unittest.main()