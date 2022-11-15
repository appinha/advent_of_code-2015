from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
import re


delimiter = "\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def _get_input(self, raw_input, init_state=False):
        reindeers = []
        for line in raw_input:
            result = re.search(r'(\w+).+(\b\d+).+(\b\d+).+(\b\d+)', line)
            reindeer = {
                "name": result.group(1),
                "speed": int(result.group(2)),
                "run_time": int(result.group(3)),
                "rest_time": int(result.group(4)),
            }
            if init_state:
                reindeer.update({
                    "curr_state": "running",
                    "elapsed_secs": 0,
                    "total_km": 0,
                    "points": 0,
                })
            reindeers.append(reindeer)
        return reindeers

    def _get_total_km_for(self, reindeer, seconds):
        total_km = 0
        while seconds > 0:
            if seconds > reindeer["run_time"]:
                total_km += reindeer["speed"] * reindeer["run_time"]
            else:
                total_km += reindeer["speed"] * seconds
            seconds -= (reindeer["run_time"] + reindeer["rest_time"])
        return total_km

    def solve_part_1(self, raw_input):
        reindeers = self._get_input(raw_input)
        top_runner = {}
        for reindeer in reindeers:
            reindeer["total_km"] = self._get_total_km_for(reindeer, 2503)
            if "total_km" not in top_runner or reindeer["total_km"] > top_runner["total_km"]:
                top_runner = reindeer
        return top_runner["total_km"]

    def _update_reindeer_state(self, reindeer):
        if reindeer["curr_state"] == "running" and reindeer["elapsed_secs"] < reindeer["run_time"]:
            reindeer["total_km"] += reindeer["speed"]

        reindeer["elapsed_secs"] += 1

        if reindeer["curr_state"] == "running" and reindeer["elapsed_secs"] == reindeer["run_time"]:
            reindeer["curr_state"] = "resting"
            reindeer["elapsed_secs"] = 0

        if reindeer["curr_state"] == "resting" and reindeer["elapsed_secs"] == reindeer["rest_time"]:
            reindeer["curr_state"] = "running"
            reindeer["elapsed_secs"] = 0

    def _award_points(self, reindeers):
        ordered_reindeers = sorted(reindeers, key=lambda d: d['total_km'])
        top_total_km = ordered_reindeers[-1]["total_km"]
        for reindeer in reindeers:
            if reindeer["total_km"] == top_total_km:
                reindeer["points"] += 1

    def _find_winner_points(self, reindeers):
        return max([reindeer["points"] for reindeer in reindeers])

    def solve_part_2(self, raw_input):
        reindeers = self._get_input(raw_input, init_state=True)
        seconds = 2503
        while seconds > 0:
            for reindeer in reindeers:
                self._update_reindeer_state(reindeer)
            self._award_points(reindeers)
            seconds -= 1
        return self._find_winner_points(reindeers)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)