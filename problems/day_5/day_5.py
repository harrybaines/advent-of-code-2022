"""
Day 5: Supply Stacks

Ref: https://adventofcode.com/2022/day/5
"""

import copy

# Starting config:
# [Q]         [N]             [N]
# [H]     [B] [D]             [S] [M]
# [C]     [Q] [J]         [V] [Q] [D]
# [T]     [S] [Z] [F]     [J] [J] [W]
# [N] [G] [T] [S] [V]     [B] [C] [C]
# [S] [B] [R] [W] [D] [J] [Q] [R] [Q]
# [V] [D] [W] [G] [P] [W] [N] [T] [S]
# [B] [W] [F] [L] [M] [F] [L] [G] [J]
# 1   2   3   4   5   6   7   8   9
STACK_CONFIG = [
    ["B", "V", "S", "N", "T", "C", "H", "Q"],
    ["W", "D", "B", "G"],
    ["F", "W", "R", "T", "S", "Q", "B"],
    ["L", "G", "W", "S", "Z", "J", "D", "N"],
    ["M", "P", "D", "V", "F"],
    ["F", "W", "J"],
    ["L", "N", "Q", "B", "J", "V"],
    ["G", "T", "R", "C", "J", "Q", "S", "N"],
    ["J", "S", "Q", "C", "W", "D", "M"],
]


class SupplyStack:
    def __init__(self, stack_config):
        self.crates = stack_config

    def push(self, n, from_stack, to_stack, version="9000"):
        if version == "9000" or (version == "9001" and n == 1):
            for _ in range(n):
                self.crates[to_stack].append(self.crates[from_stack].pop())
        elif version == "9001":
            self.crates[to_stack] = self.crates[to_stack] + self.crates[from_stack][-n:]
            del self.crates[from_stack][-n:]
        else:
            return f"ERROR: crane version {version} not supported"


def get_top_stack_crates(version):
    with open("problems/day_5/crates.txt", "r", encoding="utf-8") as f:
        supply_stack = SupplyStack(copy.deepcopy(STACK_CONFIG))
        for line in f.read().splitlines():
            words = line.split(" ")
            amount, from_stack, to_stack = list(
                map(int, [words[1], words[3], words[5]])
            )
            supply_stack.push(amount, from_stack - 1, to_stack - 1, version)
    return "".join(crate[-1] for crate in supply_stack.crates)


if __name__ == "__main__":
    # Part 1: After the rearrangement procedure completes, what crate ends up on top of each stack?
    print(get_top_stack_crates(version="9000"))
    # Answer: FJSRQCFTN

    # Part 2: After the rearrangement procedure completes, what crate ends up on top of each stack?
    print(get_top_stack_crates(version="9001"))
    # Answer: CJVLJQPHS
