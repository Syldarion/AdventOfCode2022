from util import text_file_args


DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


@text_file_args
def part1(*args):
    # [y][x]
    height = len(args[0])
    length = len(args[0][0])

    visible = 0

    for y in range(1, height - 1):
        for x in range(1, length - 1):
            for direction in DIRS:
                dx, dy = direction
                visible_in_dir = True
                base_val = args[0][y][x]
                while 0 <= y + dy < height and 0 <= x + dx < length:
                    check_val = args[0][y + dy][x + dx]
                    if check_val >= base_val:
                        visible_in_dir = False
                        break
                    dx += direction[0]
                    dy += direction[1]
                if visible_in_dir:
                    visible += 1
                    break

    # add outside grid
    visible += length * 2
    visible += (height - 2) * 2

    print(visible)


@text_file_args
def part2(*args):
    # [y][x]
    height = len(args[0])
    length = len(args[0][0])

    max_scenic_score = 0

    for y in range(0, height):
        for x in range(0, length):
            scenic_score = 1
            for direction in DIRS:
                dx, dy = direction
                visible_in_dir = 0
                base_val = args[0][y][x]
                while 0 <= y + dy < height and 0 <= x + dx < length:
                    check_val = args[0][y + dy][x + dx]
                    visible_in_dir += 1
                    if check_val >= base_val:
                        break
                    dx += direction[0]
                    dy += direction[1]
                scenic_score *= visible_in_dir
            max_scenic_score = max(max_scenic_score, scenic_score)

    print(max_scenic_score)
