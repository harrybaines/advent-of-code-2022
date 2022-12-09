"""
Day 9: Rope Bridge

Ref: https://adventofcode.com/2022/day/9
"""


def get_num_tail_rope_unique_visits(num_knots=1):
    with open("problems/day_9/motions.txt", "r", encoding="utf-8") as f:
        motions = f.read().splitlines()

        grid_size = 6
        head_x, head_y = 0, grid_size - 1
        tail_x, tail_y = None, None
        visited = set()

        def print_grid():
            for i in range(grid_size):
                for j in range(grid_size):
                    if j == head_x and i == head_y:
                        print("H", end="")
                    elif j == tail_x and i == tail_y:
                        print("T", end="")
                    else:
                        print(".", end="")
                print()
            print()

        print(f"== Initial State ==\n")
        print_grid()

        for motion in motions:
            print(f"== {motion} ==\n")
            direction, amount = motion.split(" ")
            head_y_delta, head_x_delta = 0, 0

            for _ in range(int(amount)):
                if direction == "R":
                    head_x_delta, head_y_delta = 1, 0
                elif direction == "U":
                    head_y_delta, head_x_delta = -1, 0
                elif direction == "L":
                    head_x_delta, head_y_delta = -1, 0
                elif direction == "D":
                    head_y_delta, head_x_delta = 1, 0

                # Move H
                head_x = head_x + head_x_delta
                head_y = head_y + head_y_delta

                if tail_y == head_y and tail_x == head_x:
                    print_grid()
                    continue

                # Set T starting config
                if tail_x is None:
                    tail_x, tail_y = 0, grid_size - 1
                    print_grid()
                    visited.add((tail_y, tail_x))
                    continue

                # Move T
                # If head and tail are on same row (and not overlapping)
                if (
                    tail_y == head_y
                    and not (tail_x == head_x)
                    and not (tail_y == head_y)
                ):
                    tail_x = tail_x + head_x_delta

                # If head and tail are in same column (and not overlapping)
                if (
                    tail_x == head_x
                    and not (tail_y == head_y)
                    and not (tail_x == head_x)
                ):
                    tail_y = tail_y + head_y_delta

                # Head and tail are not adjacent, so update appropriately
                if abs(tail_y - head_y) > 1 or abs(tail_x - head_x) > 1:
                    tail_y = head_y - head_y_delta
                    tail_x = head_x - head_x_delta

                visited.add((tail_y, tail_x))

                print_grid()

    return len(visited)


if __name__ == "__main__":
    # Part 1:
    # How many positions does the tail of the rope visit at least once?
    print(get_num_tail_rope_unique_visits())
    # Answer: 6376
