import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint

from collections import defaultdict


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = ""

    def _present_delivery(self, raw_input, nbr_deliverers):
        x, y = [0] * nbr_deliverers, [0] * nbr_deliverers

        qty_by_location = defaultdict(int)
        qty_by_location[(0, 0)] += nbr_deliverers

        for i, char in enumerate(raw_input):
            d = i % nbr_deliverers

            if char == '>' or char == '<':
                x[d] += 1 if char == '>' else -1
            else:
                y[d] += 1 if char == '^' else -1

            qty_by_location[(x[d], y[d])] += 1

        return len(qty_by_location)

    def solve_part_1(self, raw_input):
        return self._present_delivery(raw_input, 1)

    def solve_part_2(self, raw_input):
        return self._present_delivery(raw_input, 2)
