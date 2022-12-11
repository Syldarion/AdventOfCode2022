from util import text_file_args


MONKEYS = [
    {
        "items": [99, 67, 92, 61, 83, 64, 98],
        "op": lambda x: x * 17,
        "test": lambda x: 4 if x % 3 == 0 else 2
    },
    {
        "items": [78, 74, 88, 89, 50],
        "op": lambda x: x * 11,
        "test": lambda x: 3 if x % 5 == 0 else 5
    },
    {
        "items": [98, 91],
        "op": lambda x: x + 4,
        "test": lambda x: 6 if x % 2 == 0 else 4
    },
    {
        "items": [59, 72, 94, 91, 79, 88, 94, 51],
        "op": lambda x: x * x,
        "test": lambda x: 0 if x % 13 == 0 else 5
    },
    {
        "items": [95, 72, 78],
        "op": lambda x: x + 7,
        "test": lambda x: 7 if x % 11 == 0 else 6
    },
    {
        "items": [76],
        "op": lambda x: x + 8,
        "test": lambda x: 0 if x % 17 == 0 else 2
    },
    {
        "items": [69, 60, 53, 89, 71, 88],
        "op": lambda x: x + 5,
        "test": lambda x: 7 if x % 19 == 0 else 1
    },
    {
        "items": [72, 54, 63, 80],
        "op": lambda x: x + 3,
        "test": lambda x: 1 if x % 7 == 0 else 3
    },
]


SUPER_MOD = 3 * 5 * 2 * 13 * 11 * 17 * 19 * 7


@text_file_args
def part1(*args):
    inspected = [0, 0, 0, 0, 0, 0, 0, 0]
    for _ in range(20):
        for i, monkey in enumerate(MONKEYS):
            for j, item in enumerate(monkey["items"]):
                inspected[i] += 1
                new_value = monkey["op"](item) // 3
                to_monkey = monkey["test"](new_value)
                MONKEYS[to_monkey]["items"].append(new_value)
            monkey["items"].clear()
    inspected.sort(reverse=True)
    print(inspected)
    print(inspected[0] * inspected[1])


@text_file_args
def part2(*args):
    inspected = [0, 0, 0, 0, 0, 0, 0, 0]
    for r in range(10000):
        for i, monkey in enumerate(MONKEYS):
            for j, item in enumerate(monkey["items"]):
                inspected[i] += 1
                new_value = monkey["op"](item) % SUPER_MOD
                to_monkey = monkey["test"](new_value)
                MONKEYS[to_monkey]["items"].append(new_value)
            monkey["items"].clear()
        print(f"Round {r}: {inspected}")
    inspected.sort(reverse=True)
    print(inspected)
    print(inspected[0] * inspected[1])
