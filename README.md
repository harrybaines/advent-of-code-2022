# Advent of Code 2022

Access the problems [here](https://adventofcode.com/).

## Problems

- [x] Day 1: Calorie Counting (both parts)
- [x] Day 2: Rock Paper Scissors (both parts)
- [x] Day 3: Rucksack Reorganization (both parts)
- [x] Day 4: Camp Cleanup (both parts)
- [x] Day 5: Supply Stacks (both parts)
- [x] Day 6: Tuning Trouble (both parts)
- [x] Day 7: No Space Left On Device (both parts)
- [x] Day 8: Treetop Tree House (both parts)
- [x] Day 9: Rope Bridge (part 1)

## Usage

Create, activate and install dependencies into the new virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then run one of the examples

```bash
python problems/day_1/day_1.py
```

To run the static analysis tools:

```bash
isort problems
black problems
pylint problems
mypy problems
```