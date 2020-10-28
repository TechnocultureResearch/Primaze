""" Test Cases for Core.Core functions """
import unittest
from Core import Core


class CoreTestCase(unittest.TestCase):
    def test_double(self):
        self.assertEqual(Core.double(2), 4)

    def test_double_again(self):
        self.assertEqual(Core.double(2.2), 4.4)


if __name__ == '__main__':
    print(Core.double(20))
    unittest.main()
