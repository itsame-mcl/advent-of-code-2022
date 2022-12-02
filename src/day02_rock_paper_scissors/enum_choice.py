from enum import Enum
from functools import total_ordering


@total_ordering
class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            if self == Choice.SCISSORS and other == Choice.ROCK:
                return True
            if self == Choice.ROCK and other == Choice.SCISSORS:
                return False
            return self.value < other.value
        return NotImplemented
