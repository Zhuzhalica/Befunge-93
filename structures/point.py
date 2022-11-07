class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        """Initializing a point"""
        self.x = x
        self.y = y

    def __add__(self, other):
        """Sum of two points"""
        self.x += other.x
        self.y += other.y
        return self

    def __ne__(self, other) -> bool:
        """Checking the inequality of two points"""
        return self.x != other.x or self.y != other.y

    def __eq__(self, other) -> bool:
        """Checking the equality of two points"""
        return self.x == other.x and self.y == other.y

    def copy(self):
        return Point(self.x, self.y)
