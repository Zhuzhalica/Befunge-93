from structures.command import Command
from structures.debug import Debug
from structures.point import Point
from structures.befunge_stack import Befunge_stack
from structures.stopwatch import Stopwatch
from structures.code import Code


class Program:
    def __init__(self, path: str, debug: bool = False) -> None:
        """Initializing an empty befunge program"""

        # Execution flags
        self.PE: bool = False
        self.ASCII_mode: bool = False
        self.debug: Debug = Debug(debug)

        # Command stack
        self.stack: Befunge_stack = Befunge_stack()

        # Additional statistics
        self.__stopwatch: Stopwatch = Stopwatch()
        self.__step_count: int = 0
        self.__code_error: int = 0

        # Data about the code field
        self.__IP: Point = Point(0, 0)
        self.direction: Point = Point(1, 0)

        from system.console_io import print_program_execution_statistic
        try:
            self.code: Code = Code(path)
        except ValueError as e:
            self.end(-1)
            print_program_execution_statistic(self)
            raise e
        except FileNotFoundError as e:
            self.end(-1)
            print_program_execution_statistic(self)
            e.strerror = f"The program could not find the program " \
                         f"with the specified path"
            raise e

    def execute_command_with_stat_and_move(self) -> None:
        """Executes the current program command, move IP and
         update program statistic"""
        self.execute_command()
        self.add_step()
        self.move_IP()

    def execute_command(self) -> None:
        """Executes the current program command"""
        command: Command = self.current_command

        if self.ASCII_mode:
            if command.command != '"':
                self.stack.push(ord(command.command))
            else:
                command.execute(self)
        else:
            command.execute(self)

    @property
    def current_command(self) -> Command:
        """The field command is extracted by IP"""
        self.__IP.y %= self.code.size.y
        self.__IP.x %= self.code.size.x
        return self.code.field[self.__IP.y][self.__IP.x]

    @property
    def IP(self) -> Point:
        """The field command is extracted by IP"""
        return self.__IP

    def step_count(self) -> int:
        """Returns the current number of completed steps"""
        return self.__step_count

    def code_error(self) -> int:
        """Returns the current number of completed steps"""
        return self.__code_error

    def add_step(self, count: int = 1) -> None:
        """Increasing the number of executed commands"""
        self.__step_count += count

    def move_IP(self) -> None:
        """IP shift in the current direction"""
        self.__IP += self.direction

    def start(self) -> None:
        """Defines statistical data at the
         beginning of the program execution"""
        self.__stopwatch.start()

    def timeout(self) -> None:
        """Timeout the calculation of program statistics"""
        self.__stopwatch.timeout()

    def resume(self) -> None:
        """Resume the calculation of program statistics"""
        self.__stopwatch.resume()

    def end(self, code_error: int = 0) -> None:
        """Determines statistical data at the end of the program"""
        self.__stopwatch.stop()
        self.__code_error = code_error

    def current_execution_time(self) -> float:
        """Returns the current program execution time"""
        return self.__stopwatch.time_per_second()
