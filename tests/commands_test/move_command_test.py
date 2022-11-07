import os
import sys
import unittest

sys.path.append(os.getcwd())
from structures.program import Program
from structures.point import Point
from commands.move_command import execute

a = sys.path[0].split('\\')
a[len(a) - 1] = "programs_test\\empty.txt"
PATH = "\\".join(a)
sys.path.append(PATH)


class Move_command_tests(unittest.TestCase):
    def test_right_dir(self):
        program = Program(PATH)
        func = execute('>')
        func(program)
        self.assertEqual(Point(1, 0), program.direction)

    def test_left_dir(self):
        program = Program(PATH)
        func = execute('<')
        func(program)
        self.assertEqual(Point(-1, 0), program.direction)

    def test_up_dir(self):
        program = Program(PATH)
        func = execute('^')
        func(program)
        self.assertEqual(Point(0, -1), program.direction)

    def test_down_dir(self):
        program = Program(PATH)
        func = execute('v')
        func(program)
        self.assertEqual(Point(0, 1), program.direction)

    def test_h_pipe_zero(self):
        program = Program(PATH)
        program.stack.push(0)
        func = execute('_')
        func(program)
        self.assertEqual(Point(1, 0), program.direction)

    def test_h_pipe_empty(self):
        program = Program(PATH)
        func = execute('_')
        func(program)
        self.assertEqual(Point(1, 0), program.direction)

    def test_h_pipe_one(self):
        program = Program(PATH)
        program.stack.push(1)
        func = execute('_')
        func(program)
        self.assertEqual(Point(-1, 0), program.direction)

    def test_v_pipe_zero(self):
        program = Program(PATH)
        program.stack.push(0)
        func = execute('|')
        func(program)
        self.assertEqual(Point(0, 1), program.direction)

    def test_v_pipe_empty(self):
        program = Program(PATH)
        func = execute('|')
        func(program)
        self.assertEqual(Point(0, 1), program.direction)

    def test_v_pipe_one(self):
        program = Program(PATH)
        program.stack.push(1)
        func = execute('|')
        func(program)
        self.assertEqual(Point(0, -1), program.direction)

    def test_random_dir(self):
        program = Program(PATH)
        func = execute('?')
        func(program)
        answer = [Point(1, 0), Point(-1, 0), Point(0, -1), Point(0, 1)]
        self.assertTrue(program.direction in answer)

    def test_bridge(self):
        program = Program(PATH)
        func = execute('#')
        func(program)
        self.assertEqual(Point(1, 0), program.direction)
        self.assertEqual(Point(1, 0), program.IP)

    def test_end_program(self):
        program = Program(PATH)
        func = execute('@')
        func(program)
        self.assertTrue(program.PE)

    def test_wrong_command(self):
        self.assertIsNone(execute('p'))
