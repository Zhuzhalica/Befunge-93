import os
import sys
import unittest

sys.path.append(os.getcwd())

from structures.point import Point
from structures.program import Program
from structures.command import Command
from system.system_methods import add_path

PATH_empty = add_path(sys.path, "programs_test\\empty.txt")
PATH_beyond_X = add_path(sys.path, "programs_test\\beyond X.txt")
PATH_beyond_Y = add_path(sys.path, "programs_test\\beyond Y.txt")


class Program_tests(unittest.TestCase):
    def test_wrong_path(self):
        self.assertRaises(FileNotFoundError, Program, 'PATH')

    def test_create_no_debug(self):
        test = Program(PATH_empty)
        self.assertFalse(test.debug.is_set)

    def test_create_with_debug(self):
        test = Program(PATH_empty, True)
        self.assertTrue(test.debug.is_set)

    def test_current_command_on_field(self):
        test = Program(PATH_empty)
        test.code.field[10][10] = Command('p')
        test.direction = Point(10, 10)
        test.move_IP()
        self.assertEqual('p', test.current_command.command)

    def test_current_command_off_field(self):
        test = Program(PATH_empty)
        test.code.field[10][10] = Command('p')
        test.direction = Point(100, 50)
        test.move_IP()
        self.assertEqual('p', test.current_command.command)

    def test_default_move_IP(self):
        test = Program(PATH_empty)
        test.move_IP()
        self.assertEqual(1, test.IP.x)
        self.assertEqual(0, test.IP.y)

    def test_not_default_move_IP(self):
        test = Program(PATH_empty)
        test.code.field[0][0] = Command('v')
        test.execute_command()
        test.move_IP()
        self.assertEqual(0, test.IP.x)
        self.assertEqual(1, test.IP.y)

    def test_add_step(self):
        test = Program(PATH_empty)
        test.add_step()
        self.assertEqual(1, test.step_count())

    def test_add_step_with_count(self):
        test = Program(PATH_empty)
        test.add_step(2)
        self.assertEqual(2, test.step_count())

    def test_code_error_zero(self):
        test = Program(PATH_empty)
        test.end()
        self.assertEqual(0, test.code_error())

    def test_code_error_any(self):
        test = Program(PATH_empty)
        test.end(1)
        self.assertEqual(1, test.code_error())

    def test_execute_command_with_stat(self):
        test = Program(PATH_empty)
        test.code.field[0][0] = Command('v')
        test.execute_command_with_stat_and_move()
        self.assertEqual(1, test.step_count())
        self.assertEqual(Point(0, 1), test.direction)
        self.assertEqual(0, test.IP.x)
        self.assertEqual(1, test.IP.y)

    def test_execute_command(self):
        test = Program(PATH_empty)
        test.code.field[0][0] = Command('v')
        test.execute_command()
        self.assertEqual(Point(0, 1), test.direction)
        self.assertEqual(0, test.step_count())
        self.assertEqual(0, test.IP.x)
        self.assertEqual(0, test.IP.y)

    def test_execute_command_ASCII_mode(self):
        test = Program(PATH_empty)
        test.ASCII_mode = True
        test.code.field[0][0] = Command('v')
        test.execute_command()
        self.assertEqual(118, test.stack.top())
        self.assertEqual(Point(1, 0), test.direction)
        self.assertEqual(0, test.step_count())
        self.assertEqual(0, test.IP.x)
        self.assertEqual(0, test.IP.y)

    def test_execute_command_ASCII_mode_off(self):
        test = Program(PATH_empty)
        test.ASCII_mode = True
        test.code.field[0][0] = Command('"')
        test.execute_command()
        self.assertEqual(0, len(test.stack))
        self.assertFalse(test.ASCII_mode)
        self.assertEqual(0, test.step_count())
        self.assertEqual(0, test.IP.x)
        self.assertEqual(0, test.IP.y)

    def test_file_beyond_x(self):
        self.assertRaises(ValueError, Program, PATH_beyond_X)

    def test_file_beyond_y(self):
        self.assertRaises(ValueError, Program, PATH_beyond_Y)
