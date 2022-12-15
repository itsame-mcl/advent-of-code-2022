from re import findall
from itertools import chain


def manhattan_distance(first, second):
    return int(abs(second.real - first.real) + abs(second.imag - first.imag))


def single_row_exclusion(sensor, distance, row, output_as_range=True):
    row_distance = int(abs(row - sensor.imag))
    col_distance = max(distance - row_distance, -1)
    if col_distance > -1:
        if output_as_range:
            return range(int(sensor.real)-col_distance, int(sensor.real)+col_distance+1)
        else:
            return int(sensor.real)-col_distance, int(sensor.real)+col_distance
    else:
        return None


def compute_single_row_exclusion(path, row):
    with open(path) as file:
        excluded = list()
        included = set()
        for line in file:
            positions = findall(r'-?\d+',line)
            sensor = int(positions[0])+int(positions[1])*1j
            beacon = int(positions[2])+int(positions[3])*1j
            if int(beacon.imag) == row:
                included.add(int(beacon.real))
            distance = manhattan_distance(sensor, beacon)
            new_excluded_range = single_row_exclusion(sensor, distance, row)
            if new_excluded_range:
                excluded.append(new_excluded_range)
    excluded = set(chain.from_iterable(excluded))
    excluded.difference_update(included)
    return len(excluded)


def find_distress_beacon(path, x_y_max):
    sensors = []
    beacons = []
    with open(path) as file:
        for line in file:
            positions = findall(r'-?\d+',line)
            sensors.append(int(positions[0])+int(positions[1])*1j)
            beacons.append(int(positions[2])+int(positions[3])*1j)
    for y in range(x_y_max+1):
        excluded = list()
        for sensor, beacon in zip(sensors, beacons):
            distance = manhattan_distance(sensor, beacon)
            new_excluded_range = single_row_exclusion(sensor, distance, y, False)
            if new_excluded_range:
                excluded.append(new_excluded_range)
        excluded = sorted(excluded)
        max_excluded_x = 0
        for start, end in excluded:
            if start > max_excluded_x + 1:
                return (start - 1)*4000000 + y
            max_excluded_x = max(max_excluded_x, end)
            if max_excluded_x > x_y_max:
                break
    return None
