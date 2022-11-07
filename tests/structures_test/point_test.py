import os
import sys
import unittest

sys.path.append(os.getcwd())

from structures.point import Point


class Point_tests(unittest.TestCase):
    def test_empty_create(self):
        test = Point()
        self.assertEqual(Point(0, 0), test)

    def test_create(self):
        test = Point(1, 2)
        self.assertEqual(1, test.x)
        self.assertEqual(2, test.y)

    def test_add(self):
        test = Point(0, 2) + Point(2, 1)
        self.assertEqual(2, test.x)
        self.assertEqual(3, test.y)

    def test_ne_general_x(self):
        test1 = Point(1, 2)
        test2 = Point(1, 3)
        self.assertNotEqual(test1, test2)

    def test_ne_general_y(self):
        test1 = Point(1, 2)
        test2 = Point(3, 2)
        self.assertNotEqual(test1, test2)

    def test_ne_not_general(self):
        test1 = Point(1, 2)
        test2 = Point(2, 3)
        self.assertNotEqual(test1, test2)

    def test_eq(self):
        test1 = Point(1, 2)
        test2 = Point(1, 2)
        self.assertEqual(test1, test2)
