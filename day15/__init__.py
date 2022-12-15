import re
import sys
from collections import defaultdict
from util import text_file_args


@text_file_args
def part1(*args):
    sensor_data = []
    beacons = set()
    for line in args[0]:
        line_data = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
        sensor_pos = (int(line_data.group(1)), int(line_data.group(2)))
        beacon_pos = (int(line_data.group(3)), int(line_data.group(4)))
        distance = abs(sensor_pos[0] - beacon_pos[0]) + abs(sensor_pos[1] - beacon_pos[1])
        sensor_data.append((sensor_pos, beacon_pos, distance))
        beacons.add(beacon_pos)

    min_x = 9999999999
    max_x = -9999999999

    for data in sensor_data:
        reach_min_x = data[0][0] - data[2]
        reach_max_x = data[0][0] + data[2]
        if reach_min_x < min_x:
            min_x = reach_min_x
        if reach_max_x > max_x:
            max_x = reach_max_x

    in_range = 0
    for x in range(min_x, max_x + 1):
        check_pos = (x, 2000000)
        if check_pos in beacons:
            continue
        for sensor_pos, max_distance in [(data[0], data[2]) for data in sensor_data]:
            distance = abs(sensor_pos[0] - check_pos[0]) + abs(sensor_pos[1] - check_pos[1])
            if distance <= max_distance:
                in_range += 1
                break

    print(in_range)


def compare_ranges(a, b):
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    else:
        return 0


@text_file_args
def part2(*args):
    from functools import cmp_to_key

    sensor_data = []
    beacons = set()
    for line in args[0]:
        line_data = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
        sensor_pos = (int(line_data.group(1)), int(line_data.group(2)))
        beacon_pos = (int(line_data.group(3)), int(line_data.group(4)))
        distance = abs(sensor_pos[0] - beacon_pos[0]) + abs(sensor_pos[1] - beacon_pos[1])
        sensor_data.append((sensor_pos, beacon_pos, distance))
        beacons.add(beacon_pos)

    max_y = 4000000

    for y in range(max_y):
        sensor_ranges = defaultdict(int)
        for data in sensor_data:
            y_diff = abs(data[0][1] - y)
            if y_diff > data[2]:
                continue
            max_reach = data[2] - y_diff
            min_x = max(0, data[0][0] - max_reach)
            max_x = min(4000000, data[0][0] + max_reach)

            sensor_ranges[min_x] += 1
            sensor_ranges[max_x + 1] -= 1
            cur = 0
        for key in sorted(sensor_ranges.keys()):
            cur += sensor_ranges[key]
            if cur == 0 and key != 4000001:
                print(key * 4000000 + y)
                return
