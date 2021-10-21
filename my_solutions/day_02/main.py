from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
import itertools as it
import numpy as np

delimiter = "\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def get_box_dimensions(self, string):
        return list(map(int, string.split('x')))

    def solve_part_1(self, raw_input):
        areas = []
        for string in raw_input:
            box_dimensions = self.get_box_dimensions(string)
            sides_dimensions = list(it.combinations(box_dimensions, 2))
            sides_areas = [np.prod(dim) for dim in sides_dimensions]
            box_area = 2 * sum(sides_areas)
            slack = min(sides_areas)
            areas.append(box_area + slack)
        return sum(areas)

    def solve_part_2(self, raw_input):
        lengths = []
        for string in raw_input:
            box_dimensions = sorted(self.get_box_dimensions(string))
            wrap = 2 * (box_dimensions[0] + box_dimensions[1])
            ribbon = np.prod(box_dimensions)
            lengths.append(wrap + ribbon)
        return sum(lengths)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)