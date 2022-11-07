import os
import sys
import unittest

sys.path.append(os.getcwd())
from structures.program import Program
from commands.stack_command import execute
from structures.command import Command

a = sys.path[0].split('\\')
a[len(a) - 1] = "programs_test\\empty.txt"
PATH = "\\".join(a)
sys.path.append(PATH)


class Move_command_tests(unittest.TestCase):
    def test_ASCII_mod_on(self):
        program = Program(PATH)
        func = execute('"')
        func(program)
        self.assertTrue(program.ASCII_mode)

    def test_add_number(self):
        program = Program(PATH)
        for i in range(0, 10):
            program.code.field[0][0] = Command(str(i))
            func = execute(str(i))
            func(program)
            self.assertEqual(i, program.stack.top())

    def test_copy_empty_stack(self):
        program = Program(PATH)
        func = execute(':')
        func(program)
        self.assertEqual(0, program.stack.top())
        self.assertEqual(1, len(program.stack))

    def test_copy(self):
        program = Program(PATH)
        program.stack.push(1)
        func = execute(':')
        func(program)
        self.assertEqual(1, program.stack.top())
        self.assertEqual(2, len(program.stack))

    def test_swap_empty_stack(self):
        program = Program(PATH)
        func = execute('\\')
        func(program)
        self.assertEqual(0, program.stack.top())
        self.assertEqual(1, len(program.stack))

    def test_swap_one_args(self):
        program = Program(PATH)
        program.stack.push(1)
        func = execute('\\')
        func(program)
        self.assertEqual(2, len(program.stack))
        self.assertEqual(0, program.stack.pop())
        self.assertEqual(1, program.stack.pop())

    def test_swap_two_args(self):
        program = Program(PATH)
        program.stack.push(1)
        program.stack.push(2)
        func = execute('\\')
        func(program)
        self.assertEqual(2, len(program.stack))
        self.assertEqual(1, program.stack.pop())
        self.assertEqual(2, program.stack.pop())

    def test_del_empty_stack(self):
        program = Program(PATH)
        func = execute('$')
        func(program)
        self.assertEqual(0, len(program.stack))

    def test_del_with_element(self):
        program = Program(PATH)
        program.stack.push(1)
        func = execute('$')
        func(program)
        self.assertEqual(0, len(program.stack))

    def test_wrong_command(self):
        self.assertFalse(execute('p'))
