def letter_value(letter):
    ord_value = ord(letter)
    if 65 <= ord_value <= 90:
        return ord_value - 38
    elif 97 <= ord_value <= 122:
        return ord_value - 96
    else:
        return -1


def part1(*args):
    rucksacks = []

    with open(args[0], "r") as f:
        for line in f.readlines():
            line_strip = line.strip()
            line_len = len(line_strip)
            rucksacks.append((line_strip[:line_len//2], line_strip[line_len//2:]))

    rucksack_sum = 0
    for rucksack in rucksacks:
        compartment_intersection = set(rucksack[0]).intersection(set(rucksack[1]))
        final_letter = compartment_intersection.pop()

        value = letter_value(final_letter)

        rucksack_sum += value

    print(rucksack_sum)


def part2(*args):
    rucksack_groups = []

    with open(args[0], "r") as f:
        lines = [x.strip() for x in f.readlines()]
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
        elf_a = set(group[0])
        elf_b = set(group[1])
        elf_c = set(group[2])
        common = elf_a.intersection(elf_b.intersection(elf_c))
        final_letter = common.pop()
        value = letter_value(final_letter)
        rucksack_sum += value

    print(rucksack_sum)
