from util import text_file_args


def get_grid_data(lines):
    grid = []
    start_pos = (0, 0)
    end_pos = (0, 0)
    for y, line in enumerate(lines):
        row = []
        for x, char in enumerate(line):
            if char == "S":
                start_pos = (x, y)
                row.append(ord('a'))
            elif char == "E":
                end_pos = (x, y)
                row.append(ord('z'))
            else:
                row.append(ord(char))
        grid.append(row)
    return grid, start_pos, end_pos


def get_grid_data_p2(lines):
    grid = []
    starts = []
    end_pos = (0, 0)
    for y, line in enumerate(lines):
        row = []
        for x, char in enumerate(line):
            if char == "S" or char == "a":
                starts.append((x, y))
                row.append(ord('a'))
            elif char == "E":
                end_pos = (x, y)
                row.append(ord('z'))
            else:
                row.append(ord(char))
        grid.append(row)
    return grid, starts, end_pos


def neighbors(x, y, w, h):
    for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
        if 0 <= nx < w and 0 <= ny < h:
            yield nx, ny


def get_shortest(grid, start, end):
    steps = [(0, start[0], start[1])]
    visited = set()

    height = len(grid)
    width = len(grid[0])

    for l, x, y in steps:
        value_at_start = grid[y][x]
        if x == end[0] and y == end[1]:
            return l
        for neighbor in neighbors(x, y, width, height):
            try:
                value_at_step = grid[neighbor[1]][neighbor[0]]
                if value_at_step - value_at_start <= 1 and neighbor not in visited:
                    visited.add(neighbor)
                    steps.append((l + 1, neighbor[0], neighbor[1]))
            except IndexError:
                pass

    return 9999


@text_file_args
def part1(*args):
    grid, start, end = get_grid_data(args[0])
    print(get_shortest(grid, start, end))


@text_file_args
def part2(*args):
    grid, starts, end = get_grid_data_p2(args[0])
    lengths = []

    for start in starts:
        lengths.append(get_shortest(grid, start, end))

    print(min(lengths))
