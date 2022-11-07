import os
import sys
import unittest

sys.path.append(os.getcwd())
from structures.befunge_stack import Befunge_stack


class Befunge_stack_tests(unittest.TestCase):
    def test_empty_create(self):
        test = Befunge_stack()
        self.assertEqual(0, len(test))

    def test_create(self):
        test = Befunge_stack([1, 2])
        self.assertEqual(2, len(test))
        self.assertListEqual([1, 2], test.array)

    def test_empty_stack_top(self):
        test = Befunge_stack()
        self.assertEqual(0, test.top())
        self.assertEqual(0, len(test))

    def test_stack_top(self):
        test = Befunge_stack([1, 2])
        self.assertEqual(2, test.top())
        self.assertEqual(2, len(test))

    def test_empty_stack_pop(self):
        test = Befunge_stack()
        self.assertEqual(0, test.pop())
        self.assertEqual(0, len(test))

    def test_stack_pop(self):
        test = Befunge_stack([1, 2])
        self.assertEqual(2, test.pop())
        self.assertEqual(1, len(test))

    def test_push(self):
        test = Befunge_stack()
        test.push(2)
        self.assertEqual(1, len(test))
        self.assertEqual(2, test.pop())

    def test_empty_stack_swap(self):
        test = Befunge_stack()
        test.swap()
        self.assertEqual(0, test.top())
        self.assertEqual(1, len(test))

    def test_stack_top(self):
        test = Befunge_stack([1, 2])
        test.swap()
        self.assertListEqual([2, 1], test.array)

    def test_len(self):
        test = Befunge_stack([1, 2])
        self.assertEqual(2, len(test))
        test.pop()
        self.assertEqual(1, len(test))
