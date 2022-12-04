def get_elf_calories(file_path):
    calories = []
    with open(file_path, "r") as f:
        line = f.readline()
        current_sum = 0
        while line:
            if not line.strip():
                calories.append(current_sum)
                current_sum = 0
            else:
                current_sum += int(line)
            line = f.readline()
    return calories


def part1(*args):
    calories = get_elf_calories(args[0])
    return max(calories)


def part2(*args):
    calories = get_elf_calories(args[0])
    calories.sort(reverse=True)
    return sum(calories[:3])
