import os
import sys
import unittest

sys.path.append(os.getcwd())
from structures.program import Program
from commands.logical_command import execute

a = sys.path[0].split('\\')
a[len(a) - 1] = "programs_test\\empty.txt"
PATH = "\\".join(a)
sys.path.append(PATH)


class Logical_command_tests(unittest.TestCase):
    def test_excl_mark_one_args_one(self):
        program = Program(PATH)
        program.stack.push(1)
        func = execute('!')
        func(program)
        self.assertEqual(0, program.stack.top())

    def test_excl_mark_one_args_zero(self):
        program = Program(PATH)
        program.stack.push(0)
        func = execute('!')
        func(program)
        self.assertEqual(1, program.stack.top())

    def test_excl_mark_one_args_empty(self):
        program = Program(PATH)
        func = execute('!')
        func(program)
        self.assertEqual(1, program.stack.top())

    def test_streak_two_args_mt(self):
        program = Program(PATH)
        program.stack.push(2)
        program.stack.push(1)
        func = execute('`')
        func(program)
        self.assertEqual(1, program.stack.top())

    def test_streak_two_args_eq(self):
        program = Program(PATH)
        program.stack.push(1)
        program.stack.push(1)
        func = execute('`')
        func(program)
        self.assertEqual(0, program.stack.top())

    def test_streak_two_args_lt(self):
        program = Program(PATH)
        program.stack.push(1)
        program.stack.push(2)
        func = execute('`')
        func(program)
        self.assertEqual(0, program.stack.top())

    def test_streak_one_args_lt(self):
        program = Program(PATH)
        program.stack.push(1)
        func = execute('`')
        func(program)
        self.assertEqual(0, program.stack.top())

    def test_streak_one_args_mt(self):
        program = Program(PATH)
        program.stack.push(-1)
        func = execute('`')
        func(program)
        self.assertEqual(1, program.stack.top())

    def test_streak_zero_args(self):
        program = Program(PATH)
        func = execute('`')
        func(program)
        self.assertEqual(0, program.stack.top())

    def test_wrong_command(self):
        self.assertIsNone(execute('>'))
