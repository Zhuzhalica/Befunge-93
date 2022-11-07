from random import choice
from collections import defaultdict
from structures.point import Point
from structures.program import Program


def execute(command: str):
    """Executing commands to change the direction of befunge,
    if the command was executed returns True"""

    if command == '>':
        return right

    elif command == '<':
        return left

    elif command == '^':
        return up

    elif command == 'v':
        return down

    if command == '_':
        return down_pipe

    elif command == '|':
        return pipe

    elif command == '?':
        return random

    elif command == '#':
        return jump

    elif command == '@':
        return end

    else:
        return None


def right(program: Program):
    program.direction = Point(1, 0)


def left(program: Program):
    program.direction = Point(-1, 0)


def up(program: Program):
    program.direction = Point(0, -1)


def down(program: Program):
    program.direction = Point(0, 1)


def down_pipe(program: Program):
    a = program.stack.pop()
    if a == 0:
        program.direction = Point(1, 0)
    else:
        program.direction = Point(-1, 0)


def pipe(program: Program):
    a = program.stack.pop()
    if a == 0:
        program.direction = Point(0, 1)
    else:
        program.direction = Point(0, -1)


def random(program: Program):
    direction_vector = defaultdict(Point)
    direction_vector['>'] = Point(1, 0)
    direction_vector['<'] = Point(-1, 0)
    direction_vector['^'] = Point(0, -1)
    direction_vector['v'] = Point(0, 1)
    program.direction = choice(list(direction_vector.values()))


def jump(program: Program):
    program.move_IP()


def end(program: Program):
    program.PE = True
