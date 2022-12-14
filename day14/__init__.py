from util import text_file_args


def build_grid(paths):
    filled_positions = set()
    for path in paths:
        path_coords = path.split(" -> ")
        for idx in range(len(path_coords) - 1):
            from_coord = path_coords[idx].split(",")
            from_coord = (int(from_coord[0]), int(from_coord[1]))
            to_coord = path_coords[idx + 1].split(",")
            to_coord = (int(to_coord[0]), int(to_coord[1]))

            from_x = min(from_coord[0], to_coord[0])
            to_x = max(from_coord[0], to_coord[0])
            from_y = min(from_coord[1], to_coord[1])
            to_y = max(from_coord[1], to_coord[1])

            for x in range(from_x, to_x + 1):
                for y in range(from_y, to_y + 1):
                    filled_positions.add((x, y))

    min_x = min([pos[0] for pos in filled_positions])
    max_x = max([pos[0] for pos in filled_positions])
    min_y = min([pos[1] for pos in filled_positions])
    max_y = max([pos[1] for pos in filled_positions])

    width = max_x - min_x
    height = max_y - min_y

    grid = []
    for y in range(height):
        grid.append([])
        for x in range(width):
            grid[y].append(0)

    for position in filled_positions:
        adjusted_y = position[1] - min_y - 1
        adjusted_x = position[0] - min_x - 1
        grid[adjusted_y][adjusted_x] = 1

    return grid, min_x, min_y, width, height


@text_file_args
def part1(*args):
    grid, min_x, min_y, width, height = build_grid(args[0])
    sand_start = (500 - min_x - 1, 0)
    sand_settled = -1
    didnt_settle = False

    while not didnt_settle:
        settled = False
        sand_settled += 1
        sand_pos = sand_start
        while not settled:
            if sand_pos[1] + 1 >= height:
                didnt_settle = True
                break
            elif grid[sand_pos[1] + 1][sand_pos[0]] == 0:
                sand_pos = (sand_pos[0], sand_pos[1] + 1)
            elif sand_pos[0] - 1 < 0:
                didnt_settle = True
                break
            elif grid[sand_pos[1] + 1][sand_pos[0] - 1] == 0:
                sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)
            elif sand_pos[0] + 1 >= width:
                didnt_settle = True
                break
            elif grid[sand_pos[1] + 1][sand_pos[0] + 1] == 0:
                sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)
            else:
                grid[sand_pos[1]][sand_pos[0]] = 1
                settled = True

    print(sand_settled)


@text_file_args
def part2(*args):
    walls = set()
    for path in args[0]:
        path_coords = path.split(" -> ")
        for idx in range(len(path_coords) - 1):
            from_coord = path_coords[idx].split(",")
            from_coord = (int(from_coord[0]), int(from_coord[1]))
            to_coord = path_coords[idx + 1].split(",")
            to_coord = (int(to_coord[0]), int(to_coord[1]))

            from_x = min(from_coord[0], to_coord[0])
            to_x = max(from_coord[0], to_coord[0])
            from_y = min(from_coord[1], to_coord[1])
            to_y = max(from_coord[1], to_coord[1])

            for x in range(from_x, to_x + 1):
                for y in range(from_y, to_y + 1):
                    walls.add((x, y))

    max_y = max([pos[1] for pos in walls]) + 2

    filled = walls.copy()

    while True:
        if (500, 0) in filled:
            print(len(filled) - len(walls))
            return
        sand_x = 500
        sand_y = 0

        while True:
            if sand_y + 1 == max_y:
                filled.add((sand_x, sand_y))
                break
            if (sand_x, sand_y + 1) not in filled:
                sand_y += 1
            elif (sand_x - 1, sand_y + 1) not in filled:
                sand_y += 1
                sand_x -= 1
            elif (sand_x + 1, sand_y + 1) not in filled:
                sand_y += 1
                sand_x += 1
            else:
                filled.add((sand_x, sand_y))
                break
