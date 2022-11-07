import os
import sys
import unittest

sys.path.append(os.getcwd())

from structures.code import Code
from system.system_methods import add_path

PATH_empty = add_path(sys.path, "programs_test\\empty.txt")
PATH_beyond_X = add_path(sys.path, "programs_test\\beyond X.txt")
PATH_beyond_Y = add_path(sys.path, "programs_test\\beyond Y.txt")
PATH_Code = add_path(sys.path, "programs_test\\Code.txt")


class Code_tests(unittest.TestCase):
    def test_empty_create(self):
        code = Code(PATH_empty)
        self.assertEqual(40, len(code.field))
        self.assertEqual(90, len(code.field[0]))

    def test_wrong_path(self):
        self.assertRaises(FileNotFoundError, Code, 'PATH')

    def test_file_beyond_x(self):
        self.assertRaises(ValueError, Code, PATH_beyond_X)

    def test_file_beyond_y(self):
        self.assertRaises(ValueError, Code, PATH_beyond_Y)

    def test_right_open_file(self):
        code = Code(PATH_Code)
        with open(PATH_Code, 'r') as file:
            lines = file.readlines()

            for i in range(40):
                line = ''
                if i < len(lines):
                    line = lines[i].strip()

                for j in range(90):
                    if j < len(line) and line[j] != code.field[i][j].command:
                        self.assertFalse(True)
                    elif j >= len(line) and ' ' != code.field[i][j].command:
                        self.assertFalse(True)

        self.assertTrue(True)

    def test_size(self):
        code = Code(PATH_empty)
        self.assertEqual(90, code.size.x)
        self.assertEqual(40, code.size.y)
