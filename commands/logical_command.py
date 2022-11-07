from structures.program import Program


def execute(command: str):
    """Execution of logical commands befunge,
    if the command was executed returns True"""
    if command == '!':
        return not_top

    elif command == '`':
        return lt

    else:
        return None


def not_top(program: Program):
    a = program.stack.pop()
    if a == 0:
        program.stack.push(1)
    else:
        program.stack.push(0)


def lt(program: Program):
    a = program.stack.pop()
    b = program.stack.pop()
    if b > a:
        program.stack.push(1)
    else:
        program.stack.push(0)
