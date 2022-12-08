"""
Day 8: Treetop Tree House

Ref: https://adventofcode.com/2022/day/8
"""


def count_visible_trees():
    with open("problems/day_8/trees.txt", "r", encoding="utf-8") as f:
        trees = f.read().splitlines()
        width, height = len(trees[0]), len(trees)
        visible_trees = (height * 2) + (2 * (width - 2))

        for row_idx in range(1, width - 1):
            for col_idx in range(1, height - 1):
                tree = int(trees[row_idx][col_idx])

                # Is this tree visible from the right?
                right_trees = list(
                    map(int, [col_tree for col_tree in trees[row_idx][col_idx + 1 :]])
                )
                # Is this tree visible from the left?
                left_trees = list(
                    map(int, [col_tree for col_tree in trees[row_idx][:col_idx]])
                )
                # Is this tree visible from the bottom?
                bottom_trees = list(
                    map(int, [row_tree[col_idx] for row_tree in trees[row_idx + 1 :]])
                )
                # Is this tree visible from the top?
                top_trees = list(
                    map(int, [row_tree[col_idx] for row_tree in trees[:row_idx]])
                )

                if (
                    all(tree > right_tree for right_tree in right_trees)
                    or all(tree > left_tree for left_tree in left_trees)
                    or all(tree > bottom_tree for bottom_tree in bottom_trees)
                    or all(tree > top_tree for top_tree in top_trees)
                ):
                    visible_trees += 1

        return visible_trees


def get_highest_scenic_score():
    def count_visible_trees(subtrees):
        sub_tree_counter = 0
        for sub_tree in subtrees:
            if tree > sub_tree:
                sub_tree_counter += 1
            elif tree <= sub_tree:
                sub_tree_counter += 1
                break
        return sub_tree_counter

    with open("problems/day_8/trees.txt", "r", encoding="utf-8") as f:
        trees = f.read().splitlines()
        width, height = len(trees[0]), len(trees)
        highest_scenic_score = 0

        for row_idx in range(1, width - 1):
            for col_idx in range(1, height - 1):
                tree = int(trees[row_idx][col_idx])

                # Is this tree visible from the right?
                right_trees = list(
                    map(int, [col_tree for col_tree in trees[row_idx][col_idx + 1 :]])
                )
                # Is this tree visible from the left?
                left_trees = reversed(
                    list(map(int, [col_tree for col_tree in trees[row_idx][:col_idx]]))
                )
                # Is this tree visible from the bottom?
                bottom_trees = list(
                    map(int, [row_tree[col_idx] for row_tree in trees[row_idx + 1 :]])
                )
                # Is this tree visible from the top?
                top_trees = reversed(
                    list(map(int, [row_tree[col_idx] for row_tree in trees[:row_idx]]))
                )

                scenic_score = (
                    count_visible_trees(right_trees)
                    * count_visible_trees(left_trees)
                    * count_visible_trees(bottom_trees)
                    * count_visible_trees(top_trees)
                )

                if scenic_score > highest_scenic_score:
                    highest_scenic_score = scenic_score

    return highest_scenic_score


if __name__ == "__main__":
    # Part 1:
    # How many trees are visible from outside the grid?
    print(count_visible_trees())
    # Answer: 1669

    # Part 2:
    # What is the highest scenic score possible for any tree?
    print(get_highest_scenic_score())
    # Answer:
