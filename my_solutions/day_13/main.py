from puzzle_solver import PuzzleSolver, run_puzzle_solver
from helpers import get_unique_permutations
from pprint import pprint
from collections import defaultdict
import itertools


delimiter = "\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def _get_input(self, raw_input):
        change_by_guest_by_guest = defaultdict(dict)
        for line in raw_input:
            words = line.replace('.', '').split()
            change_by_guest_by_guest[words[0]][words[-1]] = (words[2], int(words[3]))
        return change_by_guest_by_guest

    def _get_new_input(self, raw_input):
        change_by_guest_by_guest = self._get_input(raw_input)
        for guest in change_by_guest_by_guest:
            change_by_guest_by_guest[guest].update({'Amanda': ('gain', 0)})
        guests = change_by_guest_by_guest.keys()
        change_by_guest_by_guest['Amanda'] = {guest: ('gain', 0) for guest in guests}
        return change_by_guest_by_guest

    def _get_total_happiness(self, guests, change_by_guest_by_guest):

        def get_happiness(guest, prev, next):
            changes = [change_by_guest_by_guest[guest][prev], change_by_guest_by_guest[guest][next]]
            happiness = 0
            for type, amount in changes:
                happiness += amount if type == 'gain' else -amount
            return happiness

        table = itertools.cycle(guests)
        next(table)
        prev = guests[-1]
        total_happiness = []
        for guest in guests:
            total_happiness.append(get_happiness(guest, prev, next(table)))
            prev = guest
        return sum(total_happiness)

    def _get_all_possible_total_happiness(self, change_by_guest_by_guest):
        guests = change_by_guest_by_guest.keys()
        guest_permutations = get_unique_permutations(guests)
        return [
            self._get_total_happiness(guests, change_by_guest_by_guest)
            for guests in guest_permutations
        ]

    def solve_part_1(self, raw_input):
        change_by_guest_by_guest = self._get_input(raw_input)
        return max(self._get_all_possible_total_happiness(change_by_guest_by_guest))

    def solve_part_2(self, raw_input):
        change_by_guest_by_guest = self._get_new_input(raw_input)
        return max(self._get_all_possible_total_happiness(change_by_guest_by_guest))


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)