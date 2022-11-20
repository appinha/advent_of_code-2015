import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint

import hashlib


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = ""

    def _find_decimal(self, raw_input, startswith):
        decimal = 1
        while True:
            test = raw_input + str(decimal)
            md5_hexa_hash = hashlib.md5(test.encode()).hexdigest()
            if md5_hexa_hash.startswith(startswith):
                break
            decimal += 1
        return decimal

    def solve_part_1(self, raw_input):
        return self._find_decimal(raw_input, '00000')

    def solve_part_2(self, raw_input):
        return self._find_decimal(raw_input, '000000')
