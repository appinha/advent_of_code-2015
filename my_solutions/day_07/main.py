import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint

from collections import defaultdict


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n"

    def _get_input(self, raw_input):
        instructions_by_wire = defaultdict(list)
        signal_by_wire = defaultdict(int)
        for line in raw_input:
            raw_instruction, receiver = line.split(' -> ')
            if raw_instruction.isdigit():
                signal_by_wire[receiver] = int(raw_instruction)
            else:
                instructions_by_wire[receiver] = list(map(lib.str_to_int, raw_instruction.split()))
        return instructions_by_wire, signal_by_wire

    def _follow_instructions(self, instructions_by_wire, signal_by_wire):

        def is_solvable(instruction):
            for item in instruction:
                if lib.is_str(item) and item.islower():
                    return False
            return True

        def solve(instruction):
            if len(instruction) == 1:
                return instruction[0]
            if "NOT" in instruction:
                return ~instruction[1]
            if "AND" in instruction:
                return instruction[0] & instruction[2]
            if "OR" in instruction:
                return instruction[0] | instruction[2]
            if "LSHIFT" in instruction:
                return instruction[0] << instruction[2]
            if "RSHIFT" in instruction:
                return instruction[0] >> instruction[2]

        def replace_signal_in_instruction(signal_by_wire, instruction):
            for i, item in enumerate(instruction):
                if item in signal_by_wire:
                    instruction[i] = signal_by_wire[item]

        def remove_signaled_wires(to_remove, instructions_by_wire):
            for wire in to_remove:
                if wire in instructions_by_wire:
                    del instructions_by_wire[wire]

        to_remove = []
        for wire in instructions_by_wire:
            instruction = instructions_by_wire[wire]
            replace_signal_in_instruction(signal_by_wire, instruction)
            if is_solvable(instruction):
                signal_by_wire[wire] = solve(instruction)
                to_remove.append(wire)
        remove_signaled_wires(to_remove, instructions_by_wire)

    def _assemble_circuit(self, instructions_by_wire, signal_by_wire):
        while not signal_by_wire.get("a"):
            self._follow_instructions(instructions_by_wire, signal_by_wire)
        return signal_by_wire["a"]

    def solve_part_1(self, raw_input):
        instructions_by_wire, signal_by_wire = self._get_input(raw_input)
        return self._assemble_circuit(instructions_by_wire, signal_by_wire)

    def solve_part_2(self, raw_input):
        instructions_by_wire, signal_by_wire = self._get_input(raw_input)
        signal_by_wire['b'] = 3176
        return self._assemble_circuit(instructions_by_wire, signal_by_wire)
