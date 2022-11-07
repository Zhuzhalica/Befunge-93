from sys import stdin, stdout
from structures.program import Program


def execute(command: str):
    """Executing befunge I/O commands,
    if the command was executed returns True"""
    if command == '&':
        return input_num

    elif command == '~':
        return input_symbol

    elif command == '.':
        return output_num

    elif command == ',':
        return output_symbol

    else:
        return None


def input_num(program: Program):
    a = stdin.readline().strip()
    if a.isnumeric():
        program.stack.push(int(a))
    else:
        program.end(-1)
        raise ValueError(f'The program was waiting for the input of a'
                         f' numeric value, and received an input: {a}')


def input_symbol(program: Program):
    a = stdin.readline().strip()
    program.stack.push(ord(a))


def output_num(program: Program):
    if len(program.stack) != 0:
        a = program.stack.pop()
        stdout.write(str(a) + ' ')


def output_symbol(program: Program):
    if len(program.stack) != 0:
        a = program.stack.pop()
        stdout.write(chr(a))
