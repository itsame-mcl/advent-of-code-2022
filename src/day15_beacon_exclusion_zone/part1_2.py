from re import findall
from shapely import Polygon, MultiPolygon, LineString, unary_union


def manhattan_distance(first, second):
    return int(abs(second.real - first.real) + abs(second.imag - first.imag))


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
        sensors_on_y = set()
        for line in file:
            positions = findall(r'-?\d+', line)
            beacon = int(positions[2])+int(positions[3])*1j
            if int(beacon.imag) == row:
                sensors_on_y.add(LineString([(beacon.real-0.5, row), (beacon.real+0.5, row)]))
        x_min, _, x_max, _ = polygons.envelope.bounds
        target_row = LineString([(x_min, row), (x_max, row)])
        sensors_on_y = unary_union(list(sensors_on_y))
        res = polygons.intersection(target_row)
        res = res.difference(sensors_on_y)
    return res.length + 1


def find_distress_beacon(path, x_y_max):
    polygons = unary_union(construct_polygons(path))
    grid = Polygon([(0, 0), (0, x_y_max), (x_y_max, x_y_max), (x_y_max, 0)])
    distress_beacon = grid.difference(polygons)
    distress_beacon = distress_beacon.geoms[0] if isinstance(distress_beacon, MultiPolygon) else distress_beacon
    x, y = distress_beacon.centroid.coords.xy
    return int(x[0]) * 4000000 + int(y[0])
