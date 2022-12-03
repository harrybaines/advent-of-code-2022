"""
Day 3: Rucksack Reorganization

Ref: https://adventofcode.com/2022/day/3
"""

import math

ITEM_PRIORITIES = {}

for item_code, priority in zip(range(97, 123), range(1, 27)):
    ITEM_PRIORITIES[chr(item_code)] = priority

for item_code, priority in zip(range(65, 91), range(27, 53)):
    ITEM_PRIORITIES[chr(item_code)] = priority


def compute_shared_item_priority_sum_part_1():
    with open("problems/day_3/rucksacks.txt", "r", encoding="utf-8") as f:
        rucksacks = f.read().splitlines()
        priority_sum = 0
        for rucksack in rucksacks:
            items_per_comp = math.floor(len(rucksack) / 2)
            first_comp, second_comp = (
                rucksack[:items_per_comp],
                rucksack[items_per_comp:],
            )

            common_item = None
            for item in first_comp:
                if item in second_comp:
                    common_item = item
                    break

            if common_item is None:
                return f"No common item found in rucksack compartments: {first_comp}, {second_comp}"

            item_priority = ITEM_PRIORITIES[common_item]
            priority_sum += item_priority

    return priority_sum


def compute_shared_item_priority_sum_part_2():
    with open("problems/day_3/rucksacks.txt", "r", encoding="utf-8") as f:
        rucksacks = f.read().splitlines()
        priority_sum = 0
        num_groups = math.floor(len(rucksacks) / 3)
        for group in range(num_groups):
            group_rucksacks = rucksacks[group * 3 : (group * 3) + 3]
            common_item = None
            for item in group_rucksacks[0]:
                if item in group_rucksacks[1] or item in group_rucksacks[2]:
                    common_item = item
                    break

            common_item = set(group_rucksacks[0])
            for idx in range(1, len(group_rucksacks)):
                common_item = set(group_rucksacks[idx]).intersection(common_item)

            if common_item == "":
                return f"No common item found in group rucksacks: {group_rucksacks}"

            (common_item,) = common_item
            item_priority = ITEM_PRIORITIES[common_item]
            priority_sum += item_priority

    return priority_sum


if __name__ == "__main__":
    # Part 1:
    # Find the item type that appears in both compartments of each rucksack.
    # What is the sum of the priorities of those item types?
    print(compute_shared_item_priority_sum_part_1())
    # Answer: 7908

    # Part 2:
    # Find the item type that corresponds to the badges of each three-Elf group.
    # What is the sum of the priorities of those item types?
    print(compute_shared_item_priority_sum_part_2())
    # Answer: 2838
