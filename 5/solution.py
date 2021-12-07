import re

import numpy as np

import utils.file_io


def update_table(table, points, vh_only=True):
    x0, y0, x1, y1 = points
    # x0, x1, y0, y1 = min(x0, x1), max(x0, x1), min(y0, y1), max(y0, y1)
    if vh_only and y0 != y1 and x0 != x1:
        print('diagonal', x0, y0, x1, y1)
        return table

    print('points', x0, y0, x1, y1)
    updates = max(abs(x1 - x0) + 1, abs(y1 - y0) + 1)
    update_x = np.linspace(x0, x1, updates).astype(int)
    update_y = np.linspace(y0, y1, updates).astype(int)
    print('ux', update_x, update_y)
    for xi, yi in zip(update_x, update_y):
        table[yi, xi] += 1
    print('table after', table)


def part_1():
    data = utils.file_io.read_file('input.txt')
    points = []
    for line in data:
        res = re.match(r'([\d]+),([\d]+) -> ([\d]+),([\d]+)', line).groups()
        points.append(res)
    points = np.asarray(points, dtype=int)
    max_point = np.max(points) + 1
    table = np.zeros((max_point, max_point), dtype=int)
    [update_table(table, p, vh_only=True) for p in points]
    print(table)
    print(np.where(table >= 2)[0].shape[0])


def part_2():
    data = utils.file_io.read_file('input.txt')
    points = []
    for line in data:
        res = re.match(r'([\d]+),([\d]+) -> ([\d]+),([\d]+)', line).groups()
        points.append(res)
    points = np.asarray(points, dtype=int)
    max_point = np.max(points) + 1
    table = np.zeros((max_point, max_point), dtype=int)
    [update_table(table, p, vh_only=False) for p in points]
    print(table)
    print(np.where(table >= 2)[0].shape[0])


if __name__ == '__main__':
    part_2()
