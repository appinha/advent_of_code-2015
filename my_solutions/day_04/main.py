from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
import hashlib


delimiter = ""


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def find_decimal(self, raw_input, startswith):
        decimal = 1
        while True:
            test = raw_input + str(decimal)
            md5_hexa_hash = hashlib.md5(test.encode()).hexdigest()
            if md5_hexa_hash.startswith(startswith):
                break
            decimal += 1
        return decimal

    def solve_part_1(self, raw_input):
        return self.find_decimal(raw_input, '00000')

    def solve_part_2(self, raw_input):
        return self.find_decimal(raw_input, '000000')


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)