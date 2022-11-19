from pprint import pprint


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = ""

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
