import unittest

class test_methodes_string(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('FOO', 'foo'.upper())

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # Vérifie que le split échoue lorsqu'on ne sépare pas avec un charactère
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)



