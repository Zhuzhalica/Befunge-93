class Befunge_stack:
    def __init__(self, array: list[int] = None) -> None:
        """Stack initialization for befunge programs"""
        if array is None:
            array = []
        self.array = array.copy()

    def top(self) -> int:
        """Returns the top of the stack without extracting it,
        or if the stack is empty - 0"""
        if len(self.array) != 0:
            return self.array[len(self.array) - 1]
        else:
            return 0

    def pop(self) -> int:
        """Returns the top of the stack by extracting it,
        or if the stack is empty - 0"""
        if len(self.array) != 0:
            a = self.array.pop()
        else:
            a = 0

        return a

    def push(self, element: int) -> None:
        """Adds an element to the top of the stack"""
        self.array.append(element)

    def swap(self) -> None:
        """Swap the top and under the top of the stack or
        adds 0 to the top of the stack"""
        length = len(self)
        if length >= 2:
            self.array[length - 1], self.array[length - 2] = \
                self.array[length - 2], self.array[length - 1]
        else:
            self.push(0)

    def __len__(self) -> int:
        """Outputs the number of elements in the stack"""
        return len(self.array)
