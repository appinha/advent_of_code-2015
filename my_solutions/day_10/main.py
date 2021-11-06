from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
import itertools


delimiter = ""


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def look_and_say(self, digits):
        result = ""
        for digit, occurrences in itertools.groupby(digits):
            result += str(len(list(occurrences))) + digit
        return result

    def apply_look_and_say_for(self, times, digits):
        while times:
            digits = self.look_and_say(digits)
            times -= 1
        return digits

    def solve_part_1(self, raw_input):
        times = 1 if self.is_test else 40
        return len(self.apply_look_and_say_for(times, raw_input))

    def solve_part_2(self, raw_input):
        times = 50
        return len(self.apply_look_and_say_for(times, raw_input))


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)