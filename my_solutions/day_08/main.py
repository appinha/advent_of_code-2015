from pprint import pprint

import re


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n"

    def _get_list_of_strings(self, raw_input):
        strings = []
        for line in raw_input:
            strings.append(line[1:-1])
        return strings

    def _count_code_chars(self, strings):
        counts = [len(string) for string in strings]
        return sum(counts) + 2 * len(counts)

    def _count_memory_chars(self, strings):

        def convert_code_to_memory_chars(string):
            string = string.replace('\\"', '"')
            string = re.sub(r'\\x([0-9a-f][0-9a-f])', 'H', string)
            string = string.replace('\\\\', '\\')
            return string

        def count_memory_chars(string):
            return len(convert_code_to_memory_chars(string))

        counts = [count_memory_chars(string) for string in strings]
        return sum(counts)

    def _encode_strings(self, strings):
        encoded_strings = []
        for string in strings:
            string = string.replace('\\"', '///"')
            string = string.replace('\\x', '//x')
            string = string.replace('\\', '//')
            string = '/"' + string + '/"'
            encoded_strings.append(string)
        return encoded_strings

    def solve_part_1(self, raw_input):
        strings = self._get_list_of_strings(raw_input)
        return self._count_code_chars(strings) - self._count_memory_chars(strings)

    def solve_part_2(self, raw_input):
        strings = self._get_list_of_strings(raw_input)
        encoded_strings = self._encode_strings(strings)
        return self._count_code_chars(encoded_strings) - self._count_code_chars(strings)
