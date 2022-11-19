from pprint import pprint

import itertools


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = ""

    def _look_and_say(self, digits):
        result = ""
        for digit, occurrences in itertools.groupby(digits):
            result += str(len(list(occurrences))) + digit
        return result

    def _apply_look_and_say_for(self, times, digits):
        while times:
            digits = self._look_and_say(digits)
            times -= 1
        return digits

    def solve_part_1(self, raw_input):
        times = 40
        return len(self._apply_look_and_say_for(times, raw_input))

    def solve_part_2(self, raw_input):
        times = 50
        return len(self._apply_look_and_say_for(times, raw_input))
