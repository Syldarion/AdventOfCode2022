from util import get_common_elements, text_file_args


def letter_value(letter):
    ord_value = ord(letter)
    if 65 <= ord_value <= 90:
        return ord_value - 38
    elif 97 <= ord_value <= 122:
        return ord_value - 96
    else:
        return -1


@text_file_args
def part1(*args):
    rucksacks = []
    lines = args[0]

    for line in lines:
        line_len = len(line)
        rucksacks.append((line[:line_len//2], line[line_len//2:]))

    rucksack_sum = 0
    for rucksack in rucksacks:
        compartment_intersection = get_common_elements(rucksack[0], rucksack[1])
        value = letter_value(compartment_intersection[0])
        rucksack_sum += value

    print(rucksack_sum)


@text_file_args
def part2(*args):
    rucksack_groups = []
    lines = args[0]

    index = 0

    while index < len(lines):
        rucksack_groups.append((
            lines[index],
            lines[index + 1],
            lines[index + 2]
        ))
        index += 3

    rucksack_sum = 0

    for group in rucksack_groups:
        group_intersection = get_common_elements(group[0], group[1], group[2])
        value = letter_value(group_intersection[0])
        rucksack_sum += value

    print(rucksack_sum)
