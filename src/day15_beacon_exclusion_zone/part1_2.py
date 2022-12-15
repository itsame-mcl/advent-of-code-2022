from re import findall
from shapely import Polygon, LineString, unary_union


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


def construct_polygons(path):
    polygons = list()
    with open(path) as file:
        for line in file:
            positions = findall(r'-?\d+', line)
            sensor = int(positions[0])+int(positions[1])*1j
            beacon = int(positions[2])+int(positions[3])*1j
            distance = manhattan_distance(sensor, beacon)
            polygon = Polygon([(sensor.real-distance, sensor.imag),
                               (sensor.real, sensor.imag+distance),
                               (sensor.real+distance, sensor.imag),
                               (sensor.real, sensor.imag-distance)])
            polygons.append(polygon)
    return polygons


def compute_single_row_exclusion(path, row):
    polygons = unary_union(construct_polygons(path))
    with open(path) as file:
        x_min = None
        x_max = None
        sensors_on_y = set()
        for line in file:
            positions = findall(r'-?\d+', line)
            sensor = int(positions[0])+int(positions[1])*1j
            beacon = int(positions[2])+int(positions[3])*1j
            if int(beacon.imag) == row:
                sensors_on_y.add(beacon.real)
            distance = manhattan_distance(sensor, beacon)
            if not x_min or sensor.real - distance < x_min:
                x_min = sensor.real - distance
            if not x_max or sensor.real+distance > x_max:
                x_max = sensor.real + distance
        target_row = LineString([(x_min, row), (x_max, row)])
        inter = polygons.intersection(target_row)
    return inter.length + 1 - len(sensors_on_y)


def find_distress_beacon(path, x_y_max):
    polygons = unary_union(construct_polygons(path))
    grid = Polygon([(0, 0), (0, x_y_max), (x_y_max, x_y_max), (x_y_max, 0)])
    polygons_on_grid = grid.intersection(polygons)
    distress_beacon = grid.difference(polygons_on_grid)
    x, y = distress_beacon.convex_hull.exterior.coords.xy
    return int(x[0]) * 4000000 + int(y[1])
