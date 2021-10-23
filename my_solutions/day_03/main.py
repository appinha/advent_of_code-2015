from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
from collections import defaultdict

delimiter = ""


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def present_delivery(self, raw_input, nbr_deliverers):
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
        return self.present_delivery(raw_input, 1)

    def solve_part_2(self, raw_input):
        return self.present_delivery(raw_input, 2)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)