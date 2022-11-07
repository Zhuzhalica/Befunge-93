import os
import sys
import unittest

sys.path.append(os.getcwd())
from structures.program import Program
from commands.arithmetic_command import execute

a = sys.path[0].split('\\')
a[len(a) - 1] = "programs_test\\empty.txt"
PATH = "\\".join(a)
sys.path.append(PATH)


class ArithmeticTest():
    def do_arithmetic(self, program: Program, command: str):
        func = execute(command)
        func(program)
        return program.stack.pop()

    def zero_division(self, program: Program, command: str):
        func = execute(command)
        func(program)


class Arithmetic_command_tests(unittest.TestCase):
    def test_add_two_args(self):
        program = Program(PATH)
        program.stack.push(1)
        program.stack.push(2)
        self.assertEqual(3, ArithmeticTest().do_arithmetic(program, '+'))

    def test_add_one_args(self):
        program = Program(PATH)
        program.stack.push(1)
        self.assertEqual(1, ArithmeticTest().do_arithmetic(program, '+'))

    def test_add_zero_args(self):
        program = Program(PATH)
        self.assertEqual(0, ArithmeticTest().do_arithmetic(program, '+'))

    def test_sub_two_args(self):
        program = Program(PATH)
        program.stack.push(1)
        program.stack.push(2)
        self.assertEqual(-1, ArithmeticTest().do_arithmetic(program, '-'))

    def test_sub_one_args(self):
        program = Program(PATH)
        program.stack.push(1)
        self.assertEqual(-1, ArithmeticTest().do_arithmetic(program, '-'))

    def test_sub_zero_args(self):
        program = Program(PATH)
        self.assertEqual(0, ArithmeticTest().do_arithmetic(program, '-'))

    def test_mul_two_args(self):
        program = Program(PATH)
        program.stack.push(3)
        program.stack.push(2)
        self.assertEqual(6, ArithmeticTest().do_arithmetic(program, '*'))

    def test_mul_one_args(self):
        program = Program(PATH)
        program.stack.push(1)
        self.assertEqual(0, ArithmeticTest().do_arithmetic(program, '*'))

    def test_mul_zero_args(self):
        program = Program(PATH)
        self.assertEqual(0, ArithmeticTest().do_arithmetic(program, '*'))

    def test_div_two_args(self):
        program = Program(PATH)
        program.stack.push(5)
        program.stack.push(2)
        self.assertEqual(2, ArithmeticTest().do_arithmetic(program, '/'))

    def test_div_one_args(self):
        program = Program(PATH)
        program.stack.push(5)
        self.assertEqual(0, ArithmeticTest().do_arithmetic(program, '/'))

    def test_div_zero_args(self):
        program = Program(PATH)
        self.assertRaises(ZeroDivisionError,
                          ArithmeticTest().zero_division, program, '/')

    def test_rem_two_args(self):
        program = Program(PATH)
        program.stack.push(5)
        program.stack.push(3)
        self.assertEqual(2, ArithmeticTest().do_arithmetic(program, '%'))

    def test_rem_one_args(self):
        program = Program(PATH)
        program.stack.push(5)
        self.assertEqual(0, ArithmeticTest().do_arithmetic(program, '%'))

    def test_rem_zero_args(self):
        program = Program(PATH)
        self.assertRaises(ZeroDivisionError,
                          ArithmeticTest().zero_division, program, '%')

    def test_wrong_command(self):
        self.assertIsNone(execute('p'))
