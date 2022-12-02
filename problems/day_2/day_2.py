"""
Day 2: Rock Paper Scissors

Ref: https://adventofcode.com/2022/day/2
"""

LOSE, DRAW, WIN = 0, 3, 6
SCORES = {"A": 1, "B": 2, "C": 3}


def get_total_rps_score_part_1(filename: str) -> int:
    """Computes and returns the total score for the rock paper scissors game.

    Args:
        filename (str): A file containing the strategy guide.

    Returns:
        int: the total score returned from the game.
    """
    # pylint: disable=too-many-boolean-expressions
    with open(filename, "r", encoding="utf-8") as f:
        total_score = 0
        for line in f.read().splitlines():
            opp_choice, my_choice = line.split(" ")

            # Convert my_choice to same encoding as opp_choice
            my_choice = chr(ord(my_choice) - 23)
            shape_score = SCORES[my_choice]

            if opp_choice == my_choice:
                total_score += shape_score + DRAW
            elif (
                (opp_choice == "C" and my_choice == "A")
                or (opp_choice == "A" and my_choice == "B")
                or (opp_choice == "B" and my_choice == "C")
            ):
                total_score += shape_score + WIN
            elif (
                (opp_choice == "A" and my_choice == "C")
                or (opp_choice == "B" and my_choice == "A")
                or (opp_choice == "C" and my_choice == "B")
            ):
                total_score += shape_score + LOSE

    return total_score


def get_total_rps_score_part_2(filename) -> int:
    """Computes and returns the total score for the rock paper scissors game.

    Args:
        filename (str): A file containing the strategy guide.

    Returns:
        int: the total score returned from the game.
    """
    with open(filename, "r", encoding="utf-8") as f:
        total_score = 0
        for line in f.read().splitlines():
            opp_choice, round_choice = line.split(" ")

            # Need to draw
            if round_choice == "Y":
                total_score += SCORES[opp_choice] + DRAW
            # Need to lose
            elif round_choice == "X":
                if opp_choice == "A":
                    my_choice = "C"
                elif opp_choice == "B":
                    my_choice = "A"
                elif opp_choice == "C":
                    my_choice = "B"
                total_score += SCORES[my_choice] + LOSE
            # Need to win
            elif round_choice == "Z":
                if opp_choice == "A":
                    my_choice = "B"
                elif opp_choice == "B":
                    my_choice = "C"
                elif opp_choice == "C":
                    my_choice = "A"
                total_score += SCORES[my_choice] + WIN

    return total_score


if __name__ == "__main__":
    # Part 1:
    # X: rock, Y: paper, Z: scissors
    # What would your total score be if everything goes exactly according to your strategy guide?
    print(get_total_rps_score_part_1("problems/day_2/strategy_guide.txt"))
    # Answer: 10941

    # Part 2:
    # X: need to lose, Y: need to draw, Z: need to win
    # What would your total score be if everything goes exactly according to your strategy guide?
    print(get_total_rps_score_part_2("problems/day_2/strategy_guide.txt"))
    # Answer: 13071
