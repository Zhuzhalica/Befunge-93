import os
import sys
import unittest

sys.path.append(os.getcwd())
from structures.program import Program
from commands.edit_command import execute

a = sys.path[0].split('\\')
a[len(a) - 1] = "programs_test\\empty.txt"
PATH = "\\".join(a)
sys.path.append(PATH)


class Edit_command_tests(unittest.TestCase):
    def test_p_three_args(self):
        program = Program(PATH)
        program.stack.push(2)
        program.stack.push(1)
        program.stack.push(1)
        func = execute('p')
        func(program)
        self.assertEqual('2', program.code.field[1][1].command)

    def test_p_two_args(self):
        program = Program(PATH)
        program.stack.push(1)
        program.stack.push(1)
        func = execute('p')
        func(program)
        self.assertEqual('0', program.code.field[1][1].command)

    def test_p_one_args(self):
        program = Program(PATH)
        program.stack.push(1)
        func = execute('p')
        func(program)
        self.assertEqual('0', program.code.field[1][0].command)

    def test_p_zero_args(self):
        program = Program(PATH)
        func = execute('p')
        func(program)
        self.assertEqual('0', program.code.field[0][0].command)

    def test_g_two_args_str(self):
        program = Program(PATH)
        program.code.field[1][1].command = 'p'
        program.stack.push(1)
        program.stack.push(1)
        func = execute('g')
        func(program)
        self.assertEqual(ord('p'), program.stack.top())

    def test_g_two_args_num(self):
        program = Program(PATH)
        program.code.field[1][1].command = '57'
        program.stack.push(1)
        program.stack.push(1)
        func = execute('g')
        func(program)
        self.assertEqual(57, program.stack.top())

    def test_g_one_args(self):
        program = Program(PATH)
        program.code.field[1][0].command = 'p'
        program.stack.push(1)
        func = execute('g')
        func(program)
        self.assertEqual(ord('p'), program.stack.top())

    def test_g_zero_args(self):
        program = Program(PATH)
        program.code.field[0][0].command = 'p'
        func = execute('g')
        func(program)
        self.assertEqual(ord('p'), program.stack.top())

    def test_g_off_field(self):
        program = Program(PATH)
        program.stack.push(100)
        program.stack.push(100)
        func = execute('g')
        self.assertRaises(IndexError, func, program)

    def test_wrong_command(self):
        self.assertIsNone(execute('>'))
