from structures.command import Command
from structures.size import Size


class Code:
    def __init__(self, path: str) -> None:
        """Initialize code of program"""
        self.__size: Size = Size(90, 40)
        self.field: list[list[Command]] = []

        with open(path, 'r') as file:
            lines = file.readlines()

            if len(lines) > self.__size.y:
                raise ValueError(f'The code contains {len(lines)} '
                                 f'lines, although the allowed '
                                 f'maximum is {self.__size.y}')

            lines.extend([' '] * (self.__size.y - len(lines)))

            for i in range(len(lines)):
                line = lines[i].replace('\n', '')

                if len(line) > self.__size.x:
                    raise ValueError(f'The line {i} contains {len(line)} '
                                     f'characters, although the allowed '
                                     f'maximum is {self.__size.x}')

                line += ' ' * (self.__size.x - len(line))
                self.field.append([Command(line[j]) for j in range(len(line))])

    @property
    def size(self) -> Size:
        """Get code field size"""
        return self.__size
