# Usage examples:
# make day=01
# make day=12 part=1

all:
	@PYTHONPATH=.:$PYTHONPATH python3 solve_puzzles.py $(day) "input.txt" $(part)

test:
	@PYTHONPATH=".:$PYTHONPATH" python3 solve_puzzles.py $(day) "input_test.txt" $(part)

new:
	@cp -R day_ day_$(day)/
