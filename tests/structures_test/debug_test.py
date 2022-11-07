import os
import sys
import unittest

sys.path.append(os.getcwd())

from structures.debug import Debug, debug_command_state
from structures.point import Point


class Debug_mini_command_tests(unittest.TestCase):
    def test_next(self):
        debug = Debug(True)
        state = debug.check_answer('next', Point())
        self.assertEqual(debug_command_state.COMPLETE, state)

    def test_end(self):
        debug = Debug(True)
        state = debug.check_answer('end', Point())
        self.assertEqual(debug_command_state.COMPLETE, state)
        self.assertFalse(debug.is_set)

    def test_unknown_command(self):
        debug = Debug(True)
        answer = 'unknown'
        state = debug.check_answer(answer, Point())
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(f'Unknown debug command: {answer}\n',
                         debug.last_mistake_message)


class Debug_set_breakpoint_tests(unittest.TestCase):
    IP = Point(1, 1)

    def test_without_args(self):
        debug = Debug(True)
        answer = 'setbreakpoint'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(0, len(debug.get_breakpoints()))
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(
            f'Unknown command structure SetBreakpoint: {answer}\n',
            debug.last_mistake_message)

    def test_with_one_wrong_arg(self):
        debug = Debug(True)
        answer = 'setbreakpoint 1'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(0, len(debug.get_breakpoints()))
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(
            f'Unknown command structure SetBreakpoint: {answer}\n',
            debug.last_mistake_message)

    def test_with_one_right_arg(self):
        debug = Debug(True)
        answer = 'setbreakpoint this'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.WAIT_NEW_ASK, state)
        self.assertEqual(1, len(debug.get_breakpoints()))
        self.assertIn(Point(1, 1), debug.get_breakpoints())
        self.assertFalse(debug.go_to_breakpoint())
        self.assertFalse(debug.go_to_next_breakpoint())

    def test_with_two_wrong_arg(self):
        debug = Debug(True)
        answer = 'setbreakpoint this 2'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(0, len(debug.get_breakpoints()))
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(
            f'Unknown command structure SetBreakpoint: {answer}\n',
            debug.last_mistake_message)

    def test_with_two_right_arg(self):
        debug = Debug(True)
        answer = 'setbreakpoint 1 1'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.WAIT_NEW_ASK, state)
        self.assertEqual(1, len(debug.get_breakpoints()))
        self.assertIn(Point(1, 1), debug.get_breakpoints())
        self.assertFalse(debug.go_to_breakpoint())
        self.assertFalse(debug.go_to_next_breakpoint())


class Debug_remove_breakpoint_tests(unittest.TestCase):
    IP = Point(1, 1)

    def test_without_args(self):
        debug = Debug(True)
        answer = 'removebreakpoint'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(0, len(debug.get_breakpoints()))
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(
            f'Unknown command structure RemoveBreakpoint: {answer}\n',
            debug.last_mistake_message)

    def test_with_one_wrong_arg(self):
        debug = Debug(True)
        answer = 'removebreakpoint 1'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(0, len(debug.get_breakpoints()))
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(f'Unknown command structure RemoveBreakpoint: '
                         f'{answer}\n',
                         debug.last_mistake_message)

    def test_with_one_right_arg_without_breakpoints(self):
        debug = Debug(True)
        answer = 'removebreakpoint this'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(0, len(debug.get_breakpoints()))
        self.assertEqual('Point for RemoveBreakpoint is not contained '
                         'in Breakpoints\n',
                         debug.last_mistake_message)

    def test_with_one_right_arg_with_breakpoints(self):
        debug = Debug(True)
        debug.check_answer('setbreakpoint this', self.IP)
        self.assertEqual(1, len(debug.get_breakpoints()))
        answer = 'removebreakpoint this'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.WAIT_NEW_ASK, state)
        self.assertEqual(0, len(debug.get_breakpoints()))

    def test_with_two_wrong_arg(self):
        debug = Debug(True)
        answer = 'removebreakpoint this 1'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(0, len(debug.get_breakpoints()))
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(f'Unknown command structure RemoveBreakpoint: '
                         f'{answer}\n',
                         debug.last_mistake_message)

    def test_with_two_right_arg_without_breakpoints(self):
        debug = Debug(True)
        answer = 'removebreakpoint 1 1'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(0, len(debug.get_breakpoints()))
        self.assertEqual('Point for RemoveBreakpoint is not contained '
                         'in Breakpoints\n',
                         debug.last_mistake_message)

    def test_with_two_right_arg_with_breakpoints(self):
        debug = Debug(True)
        debug.check_answer('setbreakpoint this', self.IP)
        self.assertEqual(1, len(debug.get_breakpoints()))
        answer = 'removebreakpoint 1 1'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.WAIT_NEW_ASK, state)
        self.assertEqual(0, len(debug.get_breakpoints()))


class Debug_to_next_breakpoint_tests(unittest.TestCase):
    IP = Point(1, 1)

    def test_without_breakpoints(self):
        debug = Debug(True)
        answer = 'tonextbreakpoint'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(
            'For ToNextBreakpoint is any point not contained '
            'in Breakpoints\n',
            debug.last_mistake_message)
        self.assertFalse(debug.go_to_next_breakpoint())

    def test_with_breakpoints(self):
        debug = Debug(True)
        debug.check_answer('setbreakpoint this', self.IP)
        answer = 'tonextbreakpoint'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.COMPLETE, state)
        self.assertTrue(debug.go_to_next_breakpoint())


class Debug_to_breakpoint_tests(unittest.TestCase):
    IP = Point(1, 1)

    def test_without_args_without_breakpoints(self):
        debug = Debug(True)
        answer = 'tobreakpoint'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(
            f'Unknown command structure ToBreakpoint: {answer}\n',
            debug.last_mistake_message)
        self.assertFalse(debug.go_to_breakpoint())

    def test_without_args_with_breakpoint(self):
        debug = Debug(True)
        debug.check_answer('setbreakpoint this', self.IP)
        answer = 'tobreakpoint'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(
            f'Unknown command structure ToBreakpoint: {answer}\n',
            debug.last_mistake_message)
        self.assertFalse(debug.go_to_breakpoint())

    def test_with_one_wrong_arg_with_breakpoint(self):
        debug = Debug(True)
        debug.check_answer('setbreakpoint this', self.IP)
        answer = 'tobreakpoint 1'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(
            f'Unknown command structure ToBreakpoint: {answer}\n',
            debug.last_mistake_message)
        self.assertFalse(debug.go_to_breakpoint())

    def test_with_one_wrong_arg_without_breakpoint(self):
        debug = Debug(True)
        debug.check_answer('setbreakpoint this', self.IP)
        answer = 'tobreakpoint 1'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(
            f'Unknown command structure ToBreakpoint: {answer}\n',
            debug.last_mistake_message)
        self.assertFalse(debug.go_to_breakpoint())

    def test_with_one_right_arg_without_breakpoint(self):
        debug = Debug(True)
        answer = 'tobreakpoint this'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(
            'The point for ToBreakpoint is not contained in Breakpoints\n',
            debug.last_mistake_message)
        self.assertFalse(debug.go_to_breakpoint())

    def test_with_one_right_arg_with_breakpoint(self):
        debug = Debug(True)
        debug.check_answer('setbreakpoint this', self.IP)
        answer = 'tobreakpoint this'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.COMPLETE, state)
        self.assertTrue(debug.go_to_breakpoint())

    def test_with_two_wrong_arg_with_breakpoint(self):
        debug = Debug(True)
        debug.check_answer('setbreakpoint this', self.IP)
        answer = 'tobreakpoint this 2'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(
            f'Unknown command structure ToBreakpoint: {answer}\n',
            debug.last_mistake_message)
        self.assertFalse(debug.go_to_breakpoint())

    def test_with_two_wrong_arg_without_breakpoint(self):
        debug = Debug(True)
        debug.check_answer('setbreakpoint 2 2', self.IP)
        answer = 'tobreakpoint this 2'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(
            f'Unknown command structure ToBreakpoint: {answer}\n',
            debug.last_mistake_message)
        self.assertFalse(debug.go_to_breakpoint())

    def test_with_two_right_arg_without_breakpoint(self):
        debug = Debug(True)
        answer = 'tobreakpoint 2 2'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(
            'The point for ToBreakpoint is not contained in Breakpoints\n',
            debug.last_mistake_message)
        self.assertFalse(debug.go_to_breakpoint())

    def test_with_two_right_arg_with_breakpoint(self):
        debug = Debug(True)
        debug.check_answer('setbreakpoint 2 2', self.IP)
        answer = 'tobreakpoint 2 2'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.COMPLETE, state)
        self.assertTrue(debug.go_to_breakpoint())


class Debug_to_point_tests(unittest.TestCase):
    IP = Point(1, 1)

    def test_without_args(self):
        debug = Debug(True)
        answer = 'topoint'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(Point(), debug.point())
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(f'Unknown command structure ToPoint: {answer}\n',
                         debug.last_mistake_message)

    def test_with_one_wrong_arg(self):
        debug = Debug(True)
        answer = 'topoint 1'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(Point(), debug.point())
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(f'Unknown command structure ToPoint: {answer}\n',
                         debug.last_mistake_message)

    def test_with_one_right_arg(self):
        debug = Debug(True)
        answer = 'topoint this'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.COMPLETE, state)
        self.assertEqual(self.IP, debug.point())
        self.assertTrue(debug.go_to_point())

    def test_with_two_wrong_arg(self):
        debug = Debug(True)
        answer = 'topoint this 2'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(Point(), debug.point())
        self.assertEqual(debug_command_state.NOT_FATAL_INCORRECT_COMMAND,
                         state)
        self.assertEqual(f'Unknown command structure ToPoint: {answer}\n',
                         debug.last_mistake_message)

    def test_with_two_right_arg(self):
        debug = Debug(True)
        answer = 'topoint 2 2'
        state = debug.check_answer(answer, self.IP)
        self.assertEqual(debug_command_state.COMPLETE, state)
        self.assertEqual(Point(2, 2), debug.point())
        self.assertTrue(debug.go_to_point())
