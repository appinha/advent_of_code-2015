from puzzle_solver import PuzzleSolver, run_puzzle_solver
from helpers import is_dict, is_number, is_str
from pprint import pprint
import re
import json


delimiter = ""


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def _find_all_numbers(self, string):
        return list(map(int, re.findall(r'[0-9\-]+', string)))

    def _rec_sum(self, data):
        if is_number(data): # base case 1
            return data
        if is_str(data): # base case 2
            return 0
        if is_dict(data):
            data = data.values()
            if "red" in data:
                return 0
        return sum(self._rec_sum(d) for d in data)

    def solve_part_1(self, raw_input):
        return sum(self._find_all_numbers(raw_input))

    def solve_part_2(self, raw_input):
        data = json.loads(raw_input)
        return self._rec_sum(data)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)