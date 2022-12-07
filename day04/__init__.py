import re

from util import text_file_args


def get_pairs(lines):
    pairs = []
    for line in lines:
        parts = re.split("[-,]", line)
        pairs.append(((int(parts[0]), int(parts[1])), (int(parts[2]), int(parts[3]))))
    return pairs


@text_file_args
def part1(*args):
    pairs = get_pairs(args[0])

    overlapping_pairs = 0

    for pair in pairs:
        if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
            overlapping_pairs += 1
        elif pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]:
            overlapping_pairs += 1

    print(overlapping_pairs)


@text_file_args
def part2(*args):
    pairs = get_pairs(args[0])

    overlapping_pairs = 0

    for pair in pairs:
        if pair[0][0] <= pair[1][0] <= pair[0][1]:
            overlapping_pairs += 1
        elif pair[1][0] <= pair[0][0] <= pair[1][1]:
            overlapping_pairs += 1

    print(overlapping_pairs)
