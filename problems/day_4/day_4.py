"""
Day 4: Camp Cleanup

Ref: https://adventofcode.com/2022/day/4
"""


def count_fully_contained_assignment_pairs():
    with open("problems/day_4/assignment_pairs.txt", "r", encoding="utf-8") as f:
        elf_assignments = [
            [
                list(map(int, line.split(",")[0].split("-"))),
                list(map(int, line.split(",")[1].split("-"))),
            ]
            for line in f.read().strip().splitlines()
        ]
    return sum(
        1
        for elf_pair in elf_assignments
        if (elf_pair[0][0] >= elf_pair[1][0] and elf_pair[0][1] <= elf_pair[1][1])
        or (elf_pair[1][0] >= elf_pair[0][0] and elf_pair[1][1] <= elf_pair[0][1])
    )


def count_overlapping_assignment_pairs():
    with open("problems/day_4/assignment_pairs.txt", "r", encoding="utf-8") as f:
        elf_assignments = [
            [
                list(map(int, line.split(",")[0].split("-"))),
                list(map(int, line.split(",")[1].split("-"))),
            ]
            for line in f.read().strip().splitlines()
        ]
    return sum(
        1
        for elf_pair in elf_assignments
        if (elf_pair[0][0] >= elf_pair[1][0] and elf_pair[0][0] <= elf_pair[1][1])
        or (elf_pair[1][0] >= elf_pair[0][0] and elf_pair[1][0] <= elf_pair[0][1])
    )


if __name__ == "__main__":
    # Part 1: In how many assignment pairs does one range fully contain the other?
    print(count_fully_contained_assignment_pairs())
    # Answer: 584
    # Part 2: In how many assignment pairs do the ranges overlap?
    print(count_overlapping_assignment_pairs())
    # Answer: 933
