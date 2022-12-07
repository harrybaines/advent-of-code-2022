"""
Day 7: No Space Left On Device

Ref: https://adventofcode.com/2022/day/7
"""
import copy


class File:
    def __init__(self, name, size=0, parent=None, type="file"):
        self.name = name
        self.size = size
        self.parent = parent
        self.type = type
        self.children = []
        self.dir_sum_size = 0

    def add_child(self, child):
        self.children.append(child)

    def calculate_size(self):
        for child in self.children:
            if child.type == "dir":
                child.calculate_size()
            else:
                size_to_add = child.size
                while child.parent != None:
                    child.parent.size += size_to_add
                    child = child.parent

    def calculate_dir_sum_size(self, cur_child=None, max_size=100_000):
        if cur_child == None:
            self.dir_sum_size = 0
            cur_child = self
        for child in cur_child.children:
            if child.type == "dir" and child.size <= max_size:
                self.dir_sum_size += child.size
            self.calculate_dir_sum_size(child, max_size)
        return self.dir_sum_size

    def print_tree(self, dir_counter=0):
        print("\t" * dir_counter, self)
        for child in self.children:
            child.print_tree(dir_counter + 1)

    def find_smallest_dir_to_delete(
        self, space_required, max_space, cur_min_child=None, root=None
    ):
        if root is None:
            root = self
        for child in self.children:
            if (
                child.type == "dir"
                and (max_space - (root.size - child.size)) >= space_required
            ):
                if cur_min_child == None or child.size < cur_min_child.size:
                    cur_min_child = child
                return child.find_smallest_dir_to_delete(
                    space_required, max_space, cur_min_child, root
                )
        return cur_min_child

    def __repr__(self):
        return f"{self.name} ({self.type}, size={self.size})"


def find_directories():
    root, cur_parent_file = None, None
    with open("problems/day_7/terminal_lines.txt", "r", encoding="utf-8") as f:
        terminal_lines = f.read().splitlines()
        for terminal_line in terminal_lines:
            command = terminal_line.split(" ")
            # Changing directory
            if command[1] == "cd":
                folder = command[2]
                if folder == "/":
                    root = File(name=folder, type="dir")
                    cur_parent_file = root
                else:
                    if command[2] == "..":
                        cur_parent_file = cur_parent_file.parent
                    else:
                        for child in cur_parent_file.children:
                            if child.name == folder:
                                cur_parent_file = child
                                break
            # Directory
            elif terminal_line.startswith("dir"):
                filename = command[1]
                child = File(name=filename, parent=cur_parent_file, type="dir")
                cur_parent_file.add_child(child)
            # Normal file
            elif command[1] != "ls":
                filename = command[1]
                size = int(command[0])
                child = File(name=filename, parent=cur_parent_file, size=size)
                cur_parent_file.add_child(child)

    root.calculate_size()
    root.print_tree()
    return root


if __name__ == "__main__":
    root = find_directories()

    # Part 1:
    # Find all of the directories with a total size of at most 100000.
    # What is the sum of the total sizes of those directories?
    print(root.calculate_dir_sum_size(max_size=100_000))
    # Answer: 1_315_285

    # Part 2:
    # Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update.
    # What is the total size of that directory?
    print(
        root.find_smallest_dir_to_delete(
            space_required=30_000_000, max_space=70_000_000
        ).size
    )
    # Answer: 9847279
