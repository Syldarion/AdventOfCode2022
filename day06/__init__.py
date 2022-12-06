from util import get_file_lines_stripped


def part1(*args):
    lines = get_file_lines_stripped(args[0])
    stream = lines[0]

    for i in range(len(stream) - 4):
        stream_slice = stream[i:i+4]
        if len(set(stream_slice)) == 4:
            print(i + 4)
            break


def part2(*args):
    lines = get_file_lines_stripped(args[0])
    stream = lines[0]

    for i in range(len(stream) - 14):
        stream_slice = stream[i:i+14]
        if len(set(stream_slice)) == 14:
            print(i + 14)
            break
