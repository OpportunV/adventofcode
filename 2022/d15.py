import re
from collections import namedtuple

from shapely.ops import unary_union
from shapely import Polygon

pos = namedtuple('pos', ['x', 'y'])
pair = namedtuple('pair', ['sensor', 'beacon'])


def manhattan_dist(pos1: pos, pos2: pos):
    return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)


def update_field(coord, field, val):
    if field[coord] not in ['S', 'B']:
        field[coord] = val


def part_one(inp):
    target_y = 2_000_000
    data = set()
    for line in inp:
        values = [int(d) for d in re.findall(r'-?\d+', line)]
        sensor_pos = pos(values[0], values[1])
        beacon_pos = pos(values[2], values[3])
        data.add(pair(sensor_pos, beacon_pos))
    
    impossible = set()
    for dt in data:
        dist = manhattan_dist(dt.sensor, dt.beacon)
        dy = abs(dt.sensor.y - target_y)
        if dist >= dy:
            dx = dist - dy
            impossible.update(set(range(-dx + dt.sensor.x, dt.sensor.x + dx + 1, 1)))
    
    on_target_line = filter(lambda val: val.sensor.y == target_y or val.beacon.y == target_y, data)
    return len(impossible) - len(set(map(lambda val: val.beacon, on_target_line))) - len(
        set(map(lambda val: val.sensor, on_target_line)))


def part_two(inp):
    polygons = set()
    for line in inp:
        values = [int(d) for d in re.findall(r'-?\d+', line)]
        sensor_pos = pos(values[0], values[1])
        beacon_pos = pos(values[2], values[3])
        dist = manhattan_dist(sensor_pos, beacon_pos)
        polygons.add(Polygon([
            (sensor_pos.x - dist, sensor_pos.y),
            (sensor_pos.x, sensor_pos.y + dist),
            (sensor_pos.x + dist, sensor_pos.y),
            (sensor_pos.x, sensor_pos.y - dist)
        ]))
    
    max_coord = 4_000_000
    field = Polygon([
        (0, 0),
        (0, max_coord),
        (max_coord, max_coord),
        (max_coord, 0)
    ])
    
    union = field.intersection(unary_union(list(polygons)))
    difference = field.difference(union)
    xy = difference.centroid.coords.xy
    return int(xy[0][0] * 4000000 + xy[1][0])


def main():
    with open(r'd15_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
