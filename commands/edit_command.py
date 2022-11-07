from structures.program import Program
from structures.command import Command


def execute(command: str):
    """Executing special befunge commands,
    if the command was executed, returns True"""
    if command == 'p':
        return p

    elif command == 'g':
        return g

    else:
        return None


def p(program: Program):
    y = program.stack.pop()
    x = program.stack.pop()
    if len(program.stack) != 0:
        program.code.field[y][x] = Command(f'{program.stack.pop()}')
    else:
        program.code.field[y][x] = Command('0')


def g(program: Program):
    y = program.stack.pop()
    x = program.stack.pop()
    try:
        code = program.code.field[y][x].command
        if code.isdigit():
            program.stack.push(int(code))
        else:
            program.stack.push(ord(code))
    except IndexError:
        program.end(-1)
        raise IndexError(f'With operation g, you accessed the cell '
                         f'({x}, {y}), although the field has the size '
                         f'{program.code.size.x}x{program.code.size.y}')
