import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint

import numpy as np


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n"

    def _get_box_dimensions(self, string):
        return list(map(int, string.split('x')))

    def solve_part_1(self, raw_input):
        areas = []
        for string in raw_input:
            box_dimensions = self._get_box_dimensions(string)
            side_dimensions = lib.list_combinations(box_dimensions, 2)
            side_areas = [np.prod(dim) for dim in side_dimensions]
            box_area = 2 * sum(side_areas)
            slack = min(side_areas)
            areas.append(box_area + slack)
        return sum(areas)

    def solve_part_2(self, raw_input):
        lengths = []
        for string in raw_input:
            box_dimensions = sorted(self._get_box_dimensions(string))
            wrap = 2 * (box_dimensions[0] + box_dimensions[1])
            ribbon = np.prod(box_dimensions)
            lengths.append(wrap + ribbon)
        return sum(lengths)
