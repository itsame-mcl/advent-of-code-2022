from collections import namedtuple, Counter

Proposition = namedtuple("Proposition", "elf position")


class Elf:
    def __init__(self, controller, position):
        self.controller: ElvesController = controller
        self.position: complex = position

    def get_neighbours(self):
        neighbours = {elf.position for elf in self.controller.elves if
                      self.position.real - 1 <= elf.position.real <= self.position.real + 1 and
                      self.position.imag - 1 <= elf.position.imag <= self.position.imag + 1}
        neighbours.difference_update({self.position})
        return neighbours

    def make_proposition(self):
        neighbours = self.get_neighbours()
        if len(neighbours) == 0:
            return None
        for direction in self.controller.directions:
            candidate = self.position + direction
            if (direction.real != 0 and len(neighbours.intersection({candidate-1j, candidate, candidate+1j})) == 0) or\
               (direction.imag != 0 and len(neighbours.intersection({candidate-1, candidate, candidate+1})) == 0):
                return Proposition(elf=self, position=candidate)
        return None

    def set_position(self, position: complex):
        self.position = position


class ElvesController:
    def __init__(self, path):
        self.directions = [-1j, 1j, -1+0j, 1+0j]
        self.elves = []
        with open(path) as file:
            y = 1
            for line in file:
                line = line.replace('\n', '')
                x = 1
                for char in line:
                    if char == '#':
                        self.add_elf(x + y * 1j)
                    x += 1
                y += 1

    def add_elf(self, position):
        self.elves.append(Elf(self, position))

    def do_round(self):
        propositions = self.__get_propositions()
        propositions = self.__prune_propositions(propositions)
        self.__apply_propositions(propositions)
        self.__arrange_directions()

    def compute_empty_tiles(self):
        positions = {elf.position for elf in self.elves}
        x = {position.real for position in positions}
        y = {position.imag for position in positions}
        width = max(x) - min(x) + 1
        height = max(y) - min(y) + 1
        return width * height - len(positions)

    def __get_propositions(self):
        propositions = []
        for elf in self.elves:
            new_proposition = elf.make_proposition()
            if new_proposition is not None:
                propositions.append(new_proposition)
        return propositions

    @staticmethod
    def __prune_propositions(propositions: list[Proposition]):
        proposed_positions = Counter([proposition.position for proposition in propositions])
        pruned_propositions = [proposition for proposition in propositions
                               if proposed_positions[proposition.position] == 1]
        return pruned_propositions

    @staticmethod
    def __apply_propositions(propositions: list[Proposition]):
        for proposition in propositions:
            proposition.elf.set_position(proposition.position)

    def __arrange_directions(self):
        to_move = self.directions.pop(0)
        self.directions.append(to_move)

    def __str__(self):
        str_rep = ''
        positions = {elf.position for elf in self.elves}
        x_min = int(min({position.real for position in positions}))
        x_max = int(max({position.real for position in positions}))
        y_min = int(min({position.imag for position in positions}))
        y_max = int(max({position.imag for position in positions}))
        for y in range(y_min, y_max+1):
            for x in range(x_min, x_max+1):
                if (x+y*1j) in positions:
                    str_rep = str_rep + '#'
                else:
                    str_rep = str_rep + '.'
            str_rep = str_rep + '\n'
        return str_rep
