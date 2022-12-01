"""
Day 1: Calorie Counting

Ref: https://adventofcode.com/2022/day/1
"""

from typing import List, Tuple


def read_calories(filename: str):
    """Reads in the calories from the provided file.

    Args:
        filename (str): The name of the file containing the calories.

    Returns:
        List[List[int]]: A list of lists, where each sublist corresponds to an
            elf's calories.
    """
    with open(filename, "r", encoding="utf-8") as f:
        calories = []
        elf_calories: List[int] = []
        for line in f.read().splitlines():
            if line == "":
                calories.append(elf_calories)
                elf_calories = []
            else:
                elf_calories.append(int(line))
        calories.append(elf_calories)
    return calories


def find_elf_with_max_calories(calories: List[List[int]]) -> Tuple[int, int]:
    """Finds the elf with the most calories.

    Args:
        calories (List[List[int]]): A list of lists, where each sublist corresponds to an
            elf's calories.

    Returns:
        Tuple[int, int]: A tuple containing the elf number and their total number of
            calories.
    """
    elf_idx = -1
    cur_max_calories = 0
    for elf_calories in calories:
        total_calories = sum(elf_calories)
        if total_calories > cur_max_calories:
            cur_max_calories = total_calories
            elf_idx = calories.index(elf_calories)
    return elf_idx + 1, cur_max_calories


def find_top_elfs(calories: List[List[int]], top: int = 1) -> List[Tuple[int, int]]:
    """Finds the top elves with the most calories.

    Args:
        calories (List[List[int]]): A list of lists, where each sublist corresponds to an
            elf's calories.
        top (int, optional): The total number of elves to return. Defaults to 1.

    Returns:
        List[Tuple[int, int]]: A list of tuples, where each tuple contains the elf number
            and their total number of calories.
    """
    calorie_totals = [
        (idx + 1, sum(elf_calories)) for idx, elf_calories in enumerate(calories)
    ]
    calorie_totals.sort(key=lambda x: x[1], reverse=True)
    return calorie_totals[:top]


def main():
    """Main function"""
    calories = read_calories("problems/day_1/calories.txt")

    # Part 1:
    # Find the Elf carrying the most Calories.
    # How many total Calories is that Elf carrying?
    print(find_elf_with_max_calories(calories))
    # (189, 67016)
    # Answer: Elf 189, total is 67016.

    # Part 2:
    # Find the top three Elves carrying the most Calories.
    # How many Calories are those Elves carrying in total?
    top_n_elfs = find_top_elfs(calories, 3)  # Part 2
    print(top_n_elfs, sum(x[1] for x in top_n_elfs))
    # [(189, 67016), (44, 66601), (148, 66499)] 200116
    # Answer: Elves 189, 44 and 148, total is 200116.


if __name__ == "__main__":
    main()
