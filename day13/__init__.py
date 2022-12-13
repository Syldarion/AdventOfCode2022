from util import text_file_args


def compare_sides(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1

    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]

    len_left = len(left)
    len_right = len(right)

    i = 0
    while i < len_left and i < len_right:
        c = compare_sides(left[i], right[i])
        if c == -1:
            return -1
        if c == 1:
            return 1
        i += 1

    if i == len_left and i < len_right:
        return -1
    elif i == len_right and i < len_left:
        return 1
    else:
        return 0


@text_file_args
def part1(*args):
    pairs = [
        (eval(args[0][idx]), eval(args[0][idx + 1]))
        for idx in range(0, len(args[0]), 3)
    ]

    indices = []

    for i, pair in enumerate(pairs):
        if compare_sides(pair[0], pair[1]) == -1:
            indices.append(i + 1)

    print(sum(indices))


@text_file_args
def part2(*args):
    packets = [[[2]], [[6]]]
    for i in range(0, len(args[0]), 3):
        packets.append(eval(args[0][i]))
        packets.append(eval(args[0][i + 1]))
    from functools import cmp_to_key
    packets.sort(key=cmp_to_key(lambda a, b: compare_sides(a, b)))
    divider_indices = []
    for i, packet in enumerate(packets):
        if packet == [[2]] or packet == [[6]]:
            divider_indices.append((i + 1))
    print(divider_indices[0] * divider_indices[1])

