# A & X -> ROCK
# B & Y -> PAPER
# C & Z -> SCISSORS
# Using rock = 1
# Using paper = 2
# Using scissors = 3
# Losing = 0
# Drawing = 3
# Winning = 6

MATCH_VALUES = {
    "A X": 4,   # Rock + Rock
    "A Y": 8,   # Rock + Paper
    "A Z": 3,   # Rock + Scissors
    "B X": 1,   # Paper + Rock
    "B Y": 5,   # Paper + Paper
    "B Z": 9,   # Paper + Scissors
    "C X": 7,   # Scissors + Rock
    "C Y": 2,   # Scissors + Paper
    "C Z": 6    # Scissors + Scissors
}

# X -> lose the round
# Y -> draw the round
# Z -> win the round
RESULT_VALUES = {
    "A X": 3,   # Rock + Scissors
    "A Y": 4,   # Rock + Rock
    "A Z": 8,   # Rock + Paper
    "B X": 1,   # Paper + Rock
    "B Y": 5,   # Paper + Paper
    "B Z": 9,   # Paper + Scissors
    "C X": 2,   # Scissors + Paper
    "C Y": 6,   # Scissors + Scissors
    "C Z": 7    # Scissors + Rock
}


def part01(*args):
    file_path = args[0]
    with open(file_path, "r") as f:
        rounds = f.readlines()
    guide_sum = sum([MATCH_VALUES[x.strip()] for x in rounds])
    return guide_sum


def part02(*args):
    file_path = args[0]
    with open(file_path, "r") as f:
        rounds = f.readlines()
    guide_sum = sum([RESULT_VALUES[x.strip()] for x in rounds])
    return guide_sum
