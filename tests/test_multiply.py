import unittest
from multiply.multiplication import multiply


class TestMultiply(unittest.TestCase):

    def test_add(self):
        self.assertEqual(multiply(20, 10), 200)

unittest.main()