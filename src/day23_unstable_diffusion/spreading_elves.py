from collections import deque, namedtuple, Counter

Proposition = namedtuple("Proposition", "origin destination")


class SpreadingElves:
    def __init__(self, path):
        self.directions = deque([-1j, 1j, -1+0j, 1+0j], maxlen=4)
        self.elves = set()
        self.is_steady = False
        self.rounds = 0
        with open(path) as file:
            y = 1
            for line in file:
                line = line.replace('\n', '')
                x = 1
                for char in line:
                    if char == '#':
                        self.elves.add(x + y * 1j)
                    x += 1
                y += 1

    def do_round(self, rounds=1):
        for _ in range(rounds):
            propositions = self.__get_propositions()
            propositions = self.__prune_propositions(propositions)
            if len(propositions) == 0:
                self.is_steady = True
            self.__apply_propositions(propositions)
            self.directions.rotate(-1)
            self.rounds += 1

    def run_to_steady_state(self):
        while not self.is_steady:
            self.do_round()

    def compute_empty_tiles(self):
        x_min, x_max, y_min, y_max = self.__compute_grid_limits()
        width = x_max - x_min + 1
        height = y_max - y_min + 1
        return width * height - len(self.elves)

    def __compute_grid_limits(self):
        x = {elf.real for elf in self.elves}
        y = {elf.imag for elf in self.elves}
        return int(min(x)), int(max(x)), int(min(y)), int(max(y))

    def __get_propositions(self):
        propositions = []
        for elf in self.elves:
            new_proposition = self.__make_proposition(elf)
            if new_proposition is not None:
                propositions.append(new_proposition)
        return propositions

    def __get_neighbours(self, elf):
        neighbours = {(elf.real-1+(elf.imag-1)*1j), (elf.real+(elf.imag-1)*1j), (elf.real+1+(elf.imag-1)*1j),
                      (elf.real-1+elf.imag*1j), (elf.real+1+elf.imag*1j),
                      (elf.real-1+(elf.imag+1)*1j), (elf.real+(elf.imag+1)*1j), (elf.real+1+(elf.imag+1)*1j)}
        neighbours.intersection_update(self.elves)
        return neighbours

    def __make_proposition(self, elf):
        neighbours = self.__get_neighbours(elf)
        if len(neighbours) == 0:
            return None
        for direction in self.directions:
            candidate = elf + direction
            if (direction.real != 0 and len(neighbours.intersection({candidate-1j, candidate, candidate+1j})) == 0) or\
               (direction.imag != 0 and len(neighbours.intersection({candidate-1, candidate, candidate+1})) == 0):
                return Proposition(origin=elf, destination=candidate)
        return None

    @staticmethod
    def __prune_propositions(propositions: list[Proposition]):
        proposed_positions = Counter([proposition.destination for proposition in propositions])
        return [proposition for proposition in propositions
                if proposed_positions[proposition.destination] == 1]

    def __apply_propositions(self, propositions: list[Proposition]):
        for proposition in propositions:
            self.elves.remove(proposition.origin)
            self.elves.add(proposition.destination)

    def __str__(self):
        str_rep = ''
        x_min, x_max, y_min, y_max = self.__compute_grid_limits()
        for y in range(y_min, y_max+1):
            for x in range(x_min, x_max+1):
                if (x+y*1j) in self.elves:
                    str_rep = str_rep + '#'
                else:
                    str_rep = str_rep + '.'
            str_rep = str_rep + '\n'
        return str_rep
