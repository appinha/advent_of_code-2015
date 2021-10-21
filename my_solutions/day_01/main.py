from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint


delimiter = ""


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def solve_part_1(self, raw_input):
        count = 0
        for char in raw_input:
            count += 1 if char == "(" else -1
        return count

    def solve_part_2(self, raw_input):
        count = 0
        position = 1
        for char in raw_input:
            count += 1 if char == "(" else -1
            if count == -1:
                break
            position += 1
        return position


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)