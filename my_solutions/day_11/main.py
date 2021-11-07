from puzzle_solver import PuzzleSolver, run_puzzle_solver
from helpers import groupby
from pprint import pprint
import itertools
from string import ascii_lowercase


delimiter = ""


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)
        self.alphabet_trios = self._get_sequenced_trios(ascii_lowercase)

    def _get_sequenced_trios(self, string):
        return [string[i - 3:i] for i in range(3, len(string) + 1)]

    def _get_next_char(self, char):
        return "a" if char == "z" else chr(ord(char) + 1)

    def _get_next_valid_password(self, current):
        chars = list(current)
        last = len(chars) - 1
        for i in range(len(chars)):
            if chars[i] in 'iol':
                chars[i] = self._get_next_char(chars[i])
                for j in range(i + 1, len(chars)):
                    chars[j] = "a"
                break
            if i == last:
                return self._get_next_password("".join(chars))
        return "".join(chars)

    def _get_next_password(self, current):
        chars = list(current)
        for i in reversed(range(0, len(chars))):
            chars[i] = self._get_next_char(chars[i])
            if chars[i] != "a":
                break
        return "".join(chars)

    def has_3_letter_sequence(self, password):
        for trio in self._get_sequenced_trios(password):
            if trio in self.alphabet_trios:
                return True
        return False

    def has_pairs(self, password):
        pairs = [g["element"] for g in groupby(password) if len(g["occurrences"]) > 1]
        return len(set(pairs)) > 1

    def _check_requirements(self, password):
        return self.has_3_letter_sequence(password) and self.has_pairs(password)

    def _get_new_password(self, current):
        new_password = self._get_next_valid_password(current)
        while not self._check_requirements(new_password):
            new_password = self._get_next_password(new_password)
        return new_password

    def solve_part_1(self, raw_input):
        return self._get_new_password(raw_input)

    def solve_part_2(self, raw_input):
        return self._get_new_password(self._get_new_password(raw_input))


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)