from src.day09_rope_bridge.knots import Head, Knot


class Rope:
    def __init__(self, knots):
        self.knots = []
        self.knots.append(Head())
        for _ in range(1, knots):
            self.knots.append(Knot())

    def move(self, direction):
        self.knots[0].move(direction)
        for i in range(1, len(self.knots)):
            self.knots[i].move(self.knots[i-1])

    def tail_position(self):
        return self.knots[-1].report_position()
