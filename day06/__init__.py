from util import text_file_args


@text_file_args
def part1(*args):
    lines = args[0]
    stream = lines[0]

    for i in range(len(stream) - 4):
        stream_slice = stream[i:i+4]
        if len(set(stream_slice)) == 4:
            print(i + 4)
            break


@text_file_args
def part2(*args):
    lines = args[0]
    stream = lines[0]

    for i in range(len(stream) - 14):
        stream_slice = stream[i:i+14]
        if len(set(stream_slice)) == 14:
            print(i + 14)
            break
