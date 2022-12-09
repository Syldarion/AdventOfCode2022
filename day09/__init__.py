from util import text_file_args


DIR_X = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
DIR_Y = {'L': -1, 'U': 0, 'R': 1, 'D': 0}


def move_knot(head, tail):
    dx = (head[0] - tail[0])
    dy = (head[1] - tail[1])

    if abs(dx) <= 1 and abs(dy) <= 1:
        pass
    elif abs(dx) >= 2 and abs(dy) >= 2:
        x = head[0] - 1 if tail[0] < head[0] else head[0] + 1
        y = head[1] - 1 if tail[1] < head[1] else head[1] + 1

        tail = (x, y)
    elif abs(dx) >= 2:
        tail = (head[0] - 1 if tail[0] < head[0] else head[0] + 1, head[1])
    elif abs(dy) >= 2:
        tail = (head[0], head[1] - 1 if tail[1] < head[1] else head[1] + 1)

    return tail


@text_file_args
def part1(*args):
    head_pos = (0, 0)
    tail_pos = (0, 0)

    visited = set([tail_pos])

    for line in args[0]:
        direction, steps = line.split()
        steps = int(steps)
        for _ in range(steps):
            head_pos = (head_pos[0] + DIR_X[direction], head_pos[1] + DIR_Y[direction])
            tail_pos = move_knot(head_pos, tail_pos)
            visited.add(tail_pos)
    print(len(visited))


@text_file_args
def part2(*args):
    head_pos = (0, 0)
    tails = [(0, 0) for _ in range(9)]

    visited = set([tails[8]])

    for line in args[0]:
        direction, steps = line.split()
        steps = int(steps)
        for _ in range(steps):
            head_pos = (head_pos[0] + DIR_X[direction], head_pos[1] + DIR_Y[direction])
            tails[0] = move_knot(head_pos, tails[0])
            for i in range(1, 9):
                tails[i] = move_knot(tails[i - 1], tails[i])
            visited.add(tails[8])
    print(len(visited))
