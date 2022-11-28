import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint

import re
import json


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = ""

    def _find_all_numbers(self, string):
        return list(map(int, re.findall(r'[0-9\-]+', string)))

    def _rec_sum(self, data):
        if lib.is_number(data): # base case 1
            return data
        if lib.is_str(data): # base case 2
            return 0
        if lib.is_dict(data):
            data = data.values()
            if "red" in data:
                return 0
        return sum(self._rec_sum(d) for d in data)

    def solve_part_1(self, raw_input):
        return sum(self._find_all_numbers(raw_input))

    def solve_part_2(self, raw_input):
        data = json.loads(raw_input)
        return self._rec_sum(data)
