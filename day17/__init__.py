from util import text_file_args


shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],           # horiz. line
    [(0, 1), (1, 1), (2, 1), (1, 2), (1, 0)],   # cross
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],   # l-shape
    [(0, 0), (0, 1), (0, 2), (0, 3)],           # vert. line
    [(0, 0), (1, 0), (0, 1), (1, 1)]            # square
]


@text_file_args
def part1(*args):
    jets = args[0][0]
    jets_len = len(jets)

    step = 0
    rocks = 0
    shape_index = 0
    current_jet = 0
    filled_positions = set()
    top_y = 0

    def can_fit(origin, shape):
        for offset in shape:
            position = (origin[0] + offset[0], origin[1] + offset[1])

            if position[0] < 0 or position[0] >= 7:
                return False
            if position[1] < 0:
                return False
            if position in filled_positions:
                return False
        return True

    def print_grid(origin, shape):
        filled_and_current = set(filled_positions)
        for offset in shape:
            position = (origin[0] + offset[0], origin[1] + offset[1])
            filled_and_current.add(position)

        grid_lines = []
        for y in range(top_y + 3, 0, -1):
            line = ""
            for x in range(7):
                if (x, y) in filled_and_current:
                    line += "@"
                else:
                    line += "."
            grid_lines.append(line)
        print("\n".join(grid_lines))

    rock_origin = (2, top_y + 3)

    while rocks < 2022:
        step += 1
        if step % 2 == 0:
            # even steps are fall steps
            new_origin = (rock_origin[0], rock_origin[1] - 1)
            if can_fit(new_origin, shapes[shape_index]):
                rock_origin = new_origin
            else:
                shape_height = max(offset[1] for offset in shapes[shape_index]) + 1

                for offset in shapes[shape_index]:
                    position = (rock_origin[0] + offset[0], rock_origin[1] + offset[1])
                    filled_positions.add(position)

                top_y = max(top_y, rock_origin[1] + shape_height)
                rocks += 1
                shape_index = (shape_index + 1) % 5
                rock_origin = (2, top_y + 3)
        else:            # odd steps are jet steps
            if jets[current_jet] == "<":
                new_origin = (rock_origin[0] - 1, rock_origin[1])
                if can_fit(new_origin, shapes[shape_index]):
                    rock_origin = new_origin
            else:
                new_origin = (rock_origin[0] + 1, rock_origin[1])
                if can_fit(new_origin, shapes[shape_index]):
                    rock_origin = new_origin

            current_jet = (current_jet + 1) % jets_len

        # print_grid(rock_origin, shapes[shape_index])

    print(top_y)
