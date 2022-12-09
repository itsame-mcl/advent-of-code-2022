import math
from abc import ABC


class AbstractKnot(ABC):
    def __init__(self):
        self.x = 0
        self.y = 0

    def is_touching(self, other):
        return (other.x - 1 <= self.x <= other.x + 1) and (other.y - 1 <= self.y <= other.y + 1)

    def report_position(self):
        return self.x, self.y


class Head(AbstractKnot):
    def move(self, direction):
        match direction:
            case 'U':
                self.y += 1
            case 'D':
                self.y -= 1
            case 'L':
                self.x += 1
            case 'R':
                self.x -= 1
            case _:
                raise ValueError


class Knot(AbstractKnot):
    def move(self, previous):
        x_diff = previous.x - self.x
        y_diff = previous.y - self.y
        if not self.is_touching(previous):
            self.x = self.x + math.copysign(int(x_diff != 0), x_diff)
            self.y = self.y + math.copysign(int(y_diff != 0), y_diff)
