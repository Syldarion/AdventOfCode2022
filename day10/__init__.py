from util import text_file_args


@text_file_args
def part1(*args):
    cycle_count = 0
    cycle_values = [0]
    register = 1

    for line in args[0]:
        parts = line.split()
        if parts[0] == "addx":
            cycle_count += 1
            cycle_values.append(cycle_count * register)
            cycle_count += 1
            cycle_values.append(cycle_count * register)
            register += int(parts[1])
        else:
            cycle_count += 1
            cycle_values.append(cycle_count * register)

    print(cycle_values[20])
    print(cycle_values[60])
    print(cycle_values[100])
    print(cycle_values[140])
    print(cycle_values[180])
    print(cycle_values[220])
    print(sum([cycle_values[20], cycle_values[60], cycle_values[100], cycle_values[140], cycle_values[180], cycle_values[220]]))


@text_file_args
def part2(*args):
    display = []

    cycle_count = 0
    cycle_values = []
    register = 1

    for line in args[0]:
        parts = line.split()
        if parts[0] == "addx":
            cycle_count += 1
            cycle_values.append(register)
            cycle_count += 1
            cycle_values.append(register)
            register += int(parts[1])
        else:
            cycle_count += 1
            cycle_values.append(register)

    print(cycle_values)

    for i, value in enumerate(cycle_values):
        cycle = i % 40
        if cycle - 1 <= value <= cycle + 1:
            display.append("#")
        else:
            display.append(".")

    print(display[:40])
    print(display[40:80])
    print(display[80:120])
    print(display[120:160])
    print(display[160:200])
    print(display[200:240])
