from structures.program import Program


def execute(command: str):
    """Execution of arithmetic commands befunge,
    if the command was executed returns True"""
    if command == '+':
        return add

    elif command == '-':
        return sub

    elif command == '*':
        return mul

    elif command == '/':
        return div

    elif command == '%':
        return rem

    else:
        return None


def sub(program: Program):
    a = program.stack.pop()
    b = program.stack.pop()
    program.stack.push(b - a)


def add(program: Program):
    a = program.stack.pop()
    b = program.stack.pop()
    program.stack.push(b + a)


def div(program: Program):
    a = program.stack.pop()
    b = program.stack.pop()
    program.stack.push(b // a)


def mul(program: Program):
    a = program.stack.pop()
    b = program.stack.pop()
    program.stack.push(b * a)


def rem(program: Program):
    a = program.stack.pop()
    b = program.stack.pop()
    program.stack.push(b % a)
