# Advent of Code 2022

Access the problems [here](https://adventofcode.com/).

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

## Problems

- [x] Day 1: Calorie Counting
- [x] Day 2: Rock Paper Scissors