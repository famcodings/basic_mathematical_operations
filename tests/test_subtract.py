import unittest
from subtract.subtraction import subtract


class TestSubtract(unittest.TestCase):

    def test_add(self):
        self.assertEqual(subtract(20, 10), 10)

unittest.main()