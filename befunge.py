import sys

from structures.program import Program
from system.program_execution import program_execution
from sys import stdout


sys.tracebacklimit = 0


def main() -> None:
    path: str = ''
    debug: bool = False

    for i in range(0, len(sys.argv)):
        arg = sys.argv[i]

        if '--help' in arg or '-h' in arg:
            if len(sys.argv) == 2:
                with open('help.txt', 'r', encoding="utf-8") as file:
                    for line in file.readlines():
                        stdout.write(line + '\n')
            else:
                raise ValueError("With console command --help or -h there can "
                                 "be no other commands")
            return

        if '--path=' in arg or '-p=' in arg:
            path = arg.split('=')[1]

        if '--debug' in arg or '-d' in arg:
            debug = True

    stdout.write('\n')
    program: Program = Program(path, debug)
    program_execution(program)


if __name__ == '__main__':
    main()
