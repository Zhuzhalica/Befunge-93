from structures.program import Program
from sys import stdin, stdout


def output_current_program_info(program: Program) -> None:
    stdout.write(f'Execute command: '
                 f'{program.current_command.command}\n')
    stdout.write(f'Current IP: {program.IP.x}x{program.IP.y}\n')
    stdout.write(f'New stack: {program.stack.array}\n')
    stdout.write(f'Step count: {program.step_count()}\n')
    stdout.write(f'Execution program time: '
                 f'{program.current_execution_time()}\n')


def ask_new_debug_command(program: Program) -> str:
    program.timeout()
    stdout.write('\nNext debug command:\n')
    answer = stdin.readline().strip()
    program.resume()
    return answer


def output_debug_command_mistake(message: str) -> None:
    stdout.write(message)


def print_program_execution_statistic(program: Program):
    """Displays program execution statistics"""
    stdout.write(
        f"\n\nThe program ended with the code {program.code_error()}\n")
    stdout.write(f'Execution time: '
                 f'{program.current_execution_time():0.4f}\n')
    stdout.write(f'Completed steps when executing: {program.step_count()}\n\n')
