import os
import sys
import unittest

sys.path.append(os.getcwd())

from structures.size import Size


class Code_tests(unittest.TestCase):
    def test_empty_create(self):
        size = Size()
        self.assertEqual(0, size.x)
        self.assertEqual(0, size.y)

    def test_create(self):
        size = Size(12, 34)
        self.assertEqual(12, size.x)
        self.assertEqual(34, size.y)
