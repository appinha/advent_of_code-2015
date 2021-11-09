from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
import re
from collections import defaultdict


delimiter = ""


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def find_all_numbers(self, string):
        return list(map(int, re.findall(r'[0-9\-]+', string)))

    def solve_part_1(self, raw_input):
        return sum(self.find_all_numbers(raw_input))

    def solve_part_2(self, raw_input):
        total_count = 0
        curlybrace = 0
        curr_brace = None
        found_red = False
        tmp = defaultdict(str)
        for i, char in enumerate(raw_input):
            if char in "}{[]":
                curr_brace = char
            if char == "{":
                curlybrace += 1
            elif char == "d" and raw_input[i - 1] == "e" and raw_input[i - 2] == "r":
                if curr_brace == "{" and not found_red:
                    found_red = [True, curlybrace]
            elif char == "}":
                if not found_red:
                    total_count += sum(self.find_all_numbers(tmp[curlybrace]))
                if found_red and found_red[1] == curlybrace:
                    found_red = False
                del tmp[curlybrace]
                curlybrace -= 1
            tmp[curlybrace] += char
        total_count += sum(self.find_all_numbers(tmp[curlybrace]))
        return total_count


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)