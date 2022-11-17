import sys
sys.path.insert(0, '..')
from aoc_framework.solver.puzzle_solver import PuzzleSolver
from pprint import pprint

import itertools as it
import numpy as np


delimiter = "\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self):
        self.delimiter = delimiter

    def get_input_into_self(self, raw_input):
        self.box_dimensions = [self._get_box_dimensions(s) for s in raw_input]

    def _get_box_dimensions(self, string):
        return list(map(int, string.split('x')))

    def solve_part_1(self):
        areas = []
        for dimensions in self.box_dimensions:
            side_dimensions = list(it.combinations(dimensions, 2))
            side_areas = [np.prod(dim) for dim in side_dimensions]
            box_area = 2 * sum(side_areas)
            slack = min(side_areas)
            areas.append(box_area + slack)
        return sum(areas)

    def solve_part_2(self):
        lengths = []
        for dimensions in self.box_dimensions:
            wrap = 2 * (dimensions[0] + dimensions[1])
            ribbon = np.prod(dimensions)
            lengths.append(wrap + ribbon)
        return sum(lengths)
