from enum import Enum
from functools import total_ordering


@total_ordering
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            if self == RPS.SCISSORS and other == RPS.ROCK:
                return True
            if self == RPS.ROCK and other == RPS.SCISSORS:
                return False
            return self.value < other.value
        return NotImplemented
