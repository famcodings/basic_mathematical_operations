import unittest
from add.addition import add


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 200)

unittest.main()