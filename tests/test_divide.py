import unittest
from divide.division import divide


class TestDivide(unittest.TestCase):

    def test_add(self):
        self.assertEqual(divide(20, 10), 2)

unittest.main()