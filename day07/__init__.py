import re

from util import text_file_args


def calculate_total_size(top_level):
    total_size = top_level["local_size"]
    del top_level["local_size"]
    for sub_level in top_level:
        sub_size = calculate_total_size(top_level[sub_level])
        total_size += sub_size
    top_level["total_size"] = total_size
    return total_size


def sum_of_sub_100000_dirs(top_level):
    total = 0
    if top_level["total_size"] <= 100000:
        total += top_level["total_size"]
    del top_level["total_size"]
    for sub_level in top_level:
        sub_sum = sum_of_sub_100000_dirs(top_level[sub_level])
        total += sub_sum
    return total


@text_file_args
def part1(*args):
    lines = args[0]
    structure = {
        "/": {"local_size": 0}
    }

    current_path = []

    for line in lines:
        if line.startswith("$ cd"):
            # change directory
            if line == "$ cd ..":
                current_path.pop()
            else:
                current_path.append(line[5:])
        elif line.startswith("$ ls"):
            # start listing, we can ignore this?
            pass
        elif line.startswith("dir"):
            # dir listing
            obj = structure
            for path_piece in current_path:
                obj = obj[path_piece]
            obj[line[4:]] = {"local_size": 0}
        else:
            # file listing
            obj = structure
            for path_piece in current_path:
                obj = obj[path_piece]
            file_size_str = line.split()[0]
            obj["local_size"] += int(file_size_str)

    calculate_total_size(structure["/"])
    print(structure)
    print(sum_of_sub_100000_dirs(structure["/"]))


def get_directory_sizes_over_amount(top_level, amount):
    sizes = []
    if top_level["total_size"] >= amount:
        sizes.append(top_level["total_size"])
    del top_level["total_size"]
    for sub_level in top_level:
        sizes.extend(get_directory_sizes_over_amount(top_level[sub_level], amount))
    return sizes


@text_file_args
def part2(*args):
    lines = args[0]
    structure = {
        "/": {"local_size": 0}
    }

    current_path = []

    for line in lines:
        if line.startswith("$ cd"):
            # change directory
            if line == "$ cd ..":
                current_path.pop()
            else:
                current_path.append(line[5:])
        elif line.startswith("$ ls"):
            # start listing, we can ignore this?
            pass
        elif line.startswith("dir"):
            # dir listing
            obj = structure
            for path_piece in current_path:
                obj = obj[path_piece]
            obj[line[4:]] = {"local_size": 0}
        else:
            # file listing
            obj = structure
            for path_piece in current_path:
                obj = obj[path_piece]
            file_size_str = line.split()[0]
            obj["local_size"] += int(file_size_str)

    calculate_total_size(structure["/"])

    unused_space = 70000000 - structure["/"]["total_size"]
    space_needed = 30000000 - unused_space

    directory_sizes = get_directory_sizes_over_amount(structure["/"], space_needed)
    directory_sizes.sort()

    print(directory_sizes[0])
