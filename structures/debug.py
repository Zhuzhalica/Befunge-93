from sys import stdout

from structures.point import Point
from enum import Enum


class debug_command_state(Enum):
    WAIT_NEW_ASK = 0
    COMPLETE = 1
    NOT_FATAL_INCORRECT_COMMAND = 2


# noinspection PyPep8Naming
class Debug:
    def __init__(self, is_set: bool):
        self.is_set: bool = is_set

        self.__go_to_next_breakpoint: bool = False
        self.__go_to_breakpoint: bool = False

        self.__breakpoint_to_go: Point = Point(-1, -1)
        self.__breakpoints: list[Point] = []

        self.__go_to_point: bool = False
        self.__point: Point = Point()

        self.last_mistake_message: str = ''

    def check_answer(self, answer: str, IP: Point) -> debug_command_state:
        if answer.lower() == 'next':
            return debug_command_state.COMPLETE

        elif answer.lower() == 'end':
            self.is_set = False
            return debug_command_state.COMPLETE

        elif 'setbreakpoint' in answer.lower() or "SB" in answer:
            return self.__set_breakpoint(answer, IP)

        elif 'removebreakpoint' in answer.lower() or "RB" in answer:
            return self.__remove_breakpoint(answer, IP)

        elif answer.lower() == 'tonextbreakpoint' or "TNB" in answer:
            return self.__to_next_breakpoint()

        elif 'tobreakpoint' in answer.lower() or "TB" in answer:
            return self.__to_breakpoint(answer, IP)

        elif 'topoint' in answer.lower() or "TP" in answer:
            return self.__to_point(answer, IP)

        else:
            self.last_mistake_message = f'Unknown debug command: {answer}\n'
            return debug_command_state.NOT_FATAL_INCORRECT_COMMAND

    def __set_breakpoint(self, answer: str, IP: Point) -> debug_command_state:
        try:
            self.__breakpoints.append(
                self.__parse_answer_with_point(answer, IP))
        except ValueError:
            self.last_mistake_message = \
                f'Unknown command structure SetBreakpoint: {answer}\n'
            return debug_command_state.NOT_FATAL_INCORRECT_COMMAND

        return debug_command_state.WAIT_NEW_ASK

    def __remove_breakpoint(self, answer: str,
                            IP: Point) -> debug_command_state:
        try:
            point = self.__parse_answer_with_point(answer, IP)
            if point in self.__breakpoints:
                self.__breakpoints.remove(point)
            else:
                self.last_mistake_message = \
                    'Point for RemoveBreakpoint is not contained ' \
                    'in Breakpoints\n'
                return debug_command_state.NOT_FATAL_INCORRECT_COMMAND
        except ValueError:
            self.last_mistake_message = \
                f'Unknown command structure RemoveBreakpoint: {answer}\n'
            return debug_command_state.NOT_FATAL_INCORRECT_COMMAND
        return debug_command_state.WAIT_NEW_ASK

    def __to_next_breakpoint(self) -> debug_command_state:
        if len(self.__breakpoints) == 0:
            self.last_mistake_message = \
                'For ToNextBreakpoint is any point not contained ' \
                'in Breakpoints\n'
            return debug_command_state.NOT_FATAL_INCORRECT_COMMAND

        self.__go_to_next_breakpoint = True
        return debug_command_state.COMPLETE

    def __to_breakpoint(self, answer: str, IP: Point) -> debug_command_state:
        try:
            point = \
                self.__parse_answer_with_point(answer, IP)
            if point in self.__breakpoints:
                self.__breakpoint_to_go = point
            else:
                self.last_mistake_message = \
                    'The point for ToBreakpoint is not contained ' \
                    'in Breakpoints\n'
                return debug_command_state.NOT_FATAL_INCORRECT_COMMAND
        except ValueError:
            self.last_mistake_message = \
                f'Unknown command structure ToBreakpoint: {answer}\n'
            return debug_command_state.NOT_FATAL_INCORRECT_COMMAND

        self.__go_to_breakpoint = True
        return debug_command_state.COMPLETE

    def __to_point(self, answer: str, IP: Point) -> debug_command_state:
        try:
            self.__point = self.__parse_answer_with_point(answer, IP)
        except ValueError:
            self.last_mistake_message = \
                f'Unknown command structure ToPoint: {answer}\n'
            return debug_command_state.NOT_FATAL_INCORRECT_COMMAND

        self.__go_to_point = True
        return debug_command_state.COMPLETE

    @staticmethod
    def __parse_answer_with_point(answer: str, IP: Point) -> Point:
        args = answer.split(' ')
        if len(args) == 3 and args[1].isdigit() and args[2].isdigit():
            return Point(int(args[1]), int(args[2]))
        elif len(args) == 2 and args[1].lower() == 'this':
            return IP.copy()
        raise ValueError()

    def get_breakpoints(self) -> list[Point]:
        return self.__breakpoints.copy()

    def breakpoint_to_go(self) -> Point:
        return self.__breakpoint_to_go

    def point(self) -> Point:
        return self.__point

    def go_to_point(self) -> bool:
        return self.__go_to_point

    def go_to_next_breakpoint(self) -> bool:
        return self.__go_to_next_breakpoint

    def go_to_breakpoint(self) -> bool:
        return self.__go_to_breakpoint

    def go_to_point_remove(self) -> None:
        self.__go_to_point = False

    def go_to_next_breakpoint_remove(self) -> None:
        self.__go_to_next_breakpoint = False

    def go_to_breakpoint_remove(self) -> None:
        self.__go_to_breakpoint = False
