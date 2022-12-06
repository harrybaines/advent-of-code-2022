"""
Day 6: Tuning Trouble

Ref: https://adventofcode.com/2022/day/6
"""


def find_first_start_of_packet_marker(num_characters):
    with open("problems/day_6/datastream.txt", "r") as f:
        datastream = f.readline()
        for cur_idx in range(len(datastream) - num_characters):
            prev_chars = datastream[cur_idx : cur_idx + num_characters]
            if len(set(prev_chars)) == num_characters:
                return cur_idx + num_characters


if __name__ == "__main__":
    # Part 1: How many characters need to be processed before the first start-of-packet marker is detected?
    print(find_first_start_of_packet_marker(num_characters=4))
    # Answer: 1909

    # Part 2: How many characters need to be processed before the first start-of-message marker is detected?
    print(find_first_start_of_packet_marker(num_characters=14))
    # Answer: 1909
