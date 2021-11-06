from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
from collections import defaultdict


delimiter = "\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def _get_input(self, raw_input):
        locations_by_distance = defaultdict(list)
        location_by_distance_by_location = defaultdict(dict)

        for line in raw_input:
            locations, distance = line.split(' = ')
            locations = locations.split(' to ')
            distance = int(distance)

            locations_by_distance[distance] = locations
            location_by_distance_by_location[locations[0]][distance] = locations[1]
            location_by_distance_by_location[locations[1]][distance] = locations[0]

        return locations_by_distance, location_by_distance_by_location

    def _get_shortest_path(self, raw_input):

        def get_location_by_shortest_distance(locations):
            location_by_shortest_distance = {}
            for location in locations:
                shortest_distance = min(location_by_distance_by_location[location].keys())
                location_by_shortest_distance[shortest_distance] = location
            print("get_location_by_shortest_distance")
            pprint(location_by_shortest_distance)
            return location_by_shortest_distance

        def delete_distance(shortest_distance):
            locations = locations_by_distance[shortest_distance]
            del locations_by_distance[shortest_distance]
            del location_by_distance_by_location[locations[0]][shortest_distance]
            del location_by_distance_by_location[locations[1]][shortest_distance]

        def delete_location(shortest_location):
            locations.remove(shortest_location)


        locations_by_distance, location_by_distance_by_location = self._get_input(raw_input)
        locations = list(location_by_distance_by_location.keys())

        shortest_distance = min(locations_by_distance.keys())
        shortest_distances = [shortest_distance]
        shortest_path = locations_by_distance[shortest_distance]
        delete_distance(shortest_distance)
        delete_location(shortest_path[0])
        delete_location(shortest_path[1])

        while locations:
            print()
            print("locations:", locations)
            print("shortest_path:", shortest_path)
            print("shortest_distances:", shortest_distances)
            pprint(locations_by_distance)
            pprint(location_by_distance_by_location)

            path_ends = [shortest_path[0], shortest_path[-1]]
            location_by_shortest_distance = get_location_by_shortest_distance(path_ends)

            shortest_distance = min(location_by_shortest_distance.keys())
            shortest_distances.append(shortest_distance)

            shortest_location = location_by_shortest_distance[shortest_distance]
            delete_location(shortest_location)
            next_location = location_by_distance_by_location[shortest_location][shortest_distance]
            if path_ends[0] == shortest_location:
                shortest_path.insert(0, next_location)
            else:
                shortest_path.append(next_location)
            delete_distance(shortest_distance)

        return shortest_path

    def solve_part_1(self, raw_input):
        shortest_path = self._get_shortest_path(raw_input)
        return

    def solve_part_2(self, raw_input):
        return


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)