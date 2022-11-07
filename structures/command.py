class Command:
    def __init__(self, command: str) -> None:
        self.command: str = command
        self.execute = self.__define_function_of_command(command)

    @staticmethod
    def __define_function_of_command(command: str):
        from commands import edit_command, logical_command, move_command, \
            stack_command, io_command, arithmetic_command

        res = edit_command.execute(command)

        if res is None:
            res = logical_command.execute(command)

        if res is None:
            res = move_command.execute(command)

        if res is None:
            res = stack_command.execute(command)

        if res is None:
            res = io_command.execute(command)

        if res is None:
            res = arithmetic_command.execute(command)

        if res is None:
            res = lambda p: None

        return res
