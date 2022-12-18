from util import text_file_args

DIRS = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]


@text_file_args
def part1(*args):
    cubes = set()
    for line in args[0]:
        coords = line.split(",")
        cubes.add((int(coords[0]), int(coords[1]), int(coords[2])))
    free_faces = len(cubes) * 6
    for cube in cubes:
        for direction in DIRS:
            check = (cube[0] + direction[0], cube[1] + direction[1], cube[2] + direction[2])
            if check in cubes:
                free_faces -= 1
    print(free_faces)
