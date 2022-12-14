import re

from util import text_file_args


@text_file_args
def part1(*args):
    crate_lines = args[0]
    step_lines = args[1]

    crate_queues = []
    for i, line in enumerate(crate_lines):
        crate_queues.append([c for c in line])

    for i, line in enumerate(step_lines):
        match = re.match("move (\d+) from (\d+) to (\d+)", line)
        amt = int(match.group(1))
        from_stack = int(match.group(2)) - 1
        to_stack = int(match.group(3)) - 1

        for _ in range(amt):
            crate_queues[to_stack].append(crate_queues[from_stack].pop())

    for q in crate_queues:
        print(q.pop())


@text_file_args
def part2(*args):
    crate_lines = args[0]
    step_lines = args[1]

    crate_queues = []
    for i, line in enumerate(crate_lines):
        crate_queues.append([c for c in line])

    for i, line in enumerate(step_lines):
        match = re.match("move (\d+) from (\d+) to (\d+)", line)
        amt = int(match.group(1))
        from_stack = int(match.group(2)) - 1
        to_stack = int(match.group(3)) - 1

        crate_queues[to_stack].extend(crate_queues[from_stack][-amt:])
        del crate_queues[from_stack][-amt:]

    for q in crate_queues:
        print(q.pop())
