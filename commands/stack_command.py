from structures.program import Program


def execute(command: str):
    """Executing befunge stack commands,
    if the command was executed, returns True"""
    if command == '"':
        return ASCII

    if command.isdigit():
        return numeric

    elif command == ':':
        return copy

    elif command == '\\':
        return swap

    elif command == '$':
        return delete

    else:
        return None


def numeric(program: Program):
    program.stack.push(int(program.current_command.command))


def copy(program: Program):
    program.stack.push(program.stack.top())


def swap(program: Program):
    program.stack.swap()


def delete(program: Program):
    if len(program.stack) != 0:
        program.stack.pop()


def ASCII(program: Program):
    program.ASCII_mode = not program.ASCII_mode
