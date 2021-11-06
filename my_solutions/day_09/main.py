from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
from collections import defaultdict
import itertools
import re


delimiter = "\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def _get_input(self, raw_input):
        location_by_location_by_distance = defaultdict(dict)
        for line in raw_input:
            location_1, location_2, distance = re.split(' to | = ', line)
            location_by_location_by_distance[location_1][location_2] = int(distance)
            location_by_location_by_distance[location_2][location_1] = int(distance)
        return location_by_location_by_distance

    def _get_possible_distances(self, raw_input):

        def get_unique_permutations(locations):
            reversed_permutations = set()
            for permutation in itertools.permutations(locations):
                if permutation not in reversed_permutations:
                    reversed_permutations.add(tuple(reversed(permutation)))
                    yield permutation

        def calculate_distance(locations):
            distance = 0
            for i in range(1, len(locations)):
                distance += location_by_location_by_distance[locations[i]][locations[i - 1]]
            return distance

        location_by_location_by_distance = self._get_input(raw_input)
        locations = list(location_by_location_by_distance.keys())
        permutations = list(get_unique_permutations(locations))

        distances = []
        for locations in permutations:
            distances.append(calculate_distance(locations))

        return distances

    def solve_part_1(self, raw_input):
        return min(self._get_possible_distances(raw_input))

    def solve_part_2(self, raw_input):
        return max(self._get_possible_distances(raw_input))


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)