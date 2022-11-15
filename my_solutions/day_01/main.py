import sys
sys.path.insert(0, '..')
from aoc_framework.solver.puzzle_solver import PuzzleSolver
from pprint import pprint


delimiter = ""


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self):
        self.delimiter = delimiter

    def get_input_into_self(self, raw_input):
        self.chars = raw_input

    def solve_part_1(self):
        count = 0
        for char in self.chars:
            count += 1 if char == "(" else -1
        return count

    def solve_part_2(self):
        count = 0
        position = 1
        for char in self.chars:
            count += 1 if char == "(" else -1
            if count == -1:
                break
            position += 1
        return position
