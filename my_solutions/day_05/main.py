from pprint import pprint

import re


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n"

    def _count_nice_strings(self, raw_input, check_rules):
        count = 0
        for string in raw_input:
            if check_rules(string):
                count += 1
        return count

    def solve_part_1(self, raw_input):

        def check_rules(string):
            has_vowels = sum(list(map(string.count, "aeiou"))) >= 3
            has_repeated = re.findall(r'((\w)\2{1,})', string) != []
            hasnt_forbidden = [string.find(s) < 0 for s in ['ab', 'cd', 'pq', 'xy']]

            return has_vowels and has_repeated and all(hasnt_forbidden)

        return self._count_nice_strings(raw_input, check_rules)

    def solve_part_2(self, raw_input):

        def check_rules(string):
            has_pairs = re.findall(r'(\w{2}).*?(\1)', string) != []

            has_repeated = False
            i = 2
            while i < len(string):
                if string[i] == string[i - 2]:
                    has_repeated = True
                i += 1

            return has_pairs and has_repeated

        return self._count_nice_strings(raw_input, check_rules)
