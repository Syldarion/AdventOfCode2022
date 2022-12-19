from copy import deepcopy
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


@text_file_args
def part2(*args):
    cubes = set()
    for line in args[0]:
        coords = line.split(",")
        cubes.add((int(coords[0]), int(coords[1]), int(coords[2])))

    min_x = min_y = min_z = 999999
    max_x = max_y = max_z = 0

    for cube in cubes:
        if cube[0] < min_x:
            min_x = cube[0]
        if cube[0] > max_x:
            max_x = cube[0]
        if cube[1] < min_y:
            min_y = cube[1]
        if cube[1] > max_y:
            max_y = cube[1]
        if cube[2] < min_z:
            min_z = cube[2]
        if cube[2] > max_z:
            max_z = cube[2]

    # we want to find every air pocket that can reach the outside
    # then we can use those to see what faces actually reach the outside

    # air grid positions that touch the outside of the grid
    reaches_outside = set()
    visited = set()

    # start with the positions on the outside of the grid
    for x in [min_x, max_y]:
        for y in [min_y, max_y]:
            for z in [min_z, max_z]:
                if (x, y, z) not in cubes:
                    reaches_outside.add((x, y, z))
                    visited.add((x, y, z))

    new_added = True

    while new_added:
        new_added = False
        new_reach = set()

        # go through every reaches position and add neighbors that reach
        for position in reaches_outside:
            for direction in DIRS:
                check = (position[0] + direction[0], position[1] + direction[1], position[2] + direction[2])

                if check[0] < min_x - 1 or check[1] < min_y - 1 or check[2] < min_z - 1:
                    continue
                if check[0] > max_x + 1 or check[1] > max_y + 1 or check[2] > max_z + 1:
                    continue

                if check not in visited and check not in reaches_outside and check not in cubes:
                    new_added = True
                    new_reach.add(check)
                visited.add(check)

        reaches_outside = reaches_outside.union(new_reach)

    free_faces = len(cubes) * 6
    for cube in cubes:
        print(f"Checking {cube}")
        for direction in DIRS:
            check = (cube[0] + direction[0], cube[1] + direction[1], cube[2] + direction[2])
            if not check in reaches_outside:
                free_faces -= 1

    print(free_faces)
