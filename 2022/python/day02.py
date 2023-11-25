win = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

draw = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

loose = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

win_score = 6
draw_score = 3

def get_input_strategies():
    with open("2022/data/day02.txt") as f:
        return [l.strip().split(" ") for l in f.readlines()]

def get_score_for_round(opp, you) -> int:
    if draw[opp] == you:
        # Draw
        return score[you] + draw_score
    elif win[opp] == you:
        # Win
        return score[you] + win_score
    else:
        # loose
        return score[you]


def get_score_for_round_strat(opp, you):
    if you == "X":
        return score[loose[opp]]
    elif you == "Y":
        return score[draw[opp]] + draw_score
    else:
        return score[win[opp]] + win_score

def get_total_score():
    return sum([get_score_for_round(round[0], round[1]) for round in get_input_strategies()])

def get_total_score_correct_strat():
    return sum([get_score_for_round_strat(round[0], round[1]) for round in get_input_strategies()])


if __name__ == "__main__":
    print(get_total_score())
    print(get_total_score_correct_strat())
