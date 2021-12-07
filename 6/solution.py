import time

import numpy as np

import utils.file_io


def part_1():
    data = [int(d) for d in utils.file_io.read_file('input_ex.txt')[0].split(',')]
    data = np.array(data)

    for epoch in range(80):
        babys = len(np.where(data == 0)[0])
        data[np.where(data == 0)] = 7
        data = np.append(data, np.ones((babys,), dtype=int) * 9)
        data = data - 1

    print(len(data))


def part_2():
    data = [int(d) for d in utils.file_io.read_file('input.txt')[0].split(',')]
    data = np.array(data)

    ages = {a: 0 for a in range(10)}
    for d in data:
        ages[d] += 1
    print(ages)
    for epoch in range(256):
        babys = ages[0]
        ages[7] += babys
        ages[9] += babys
        for i in range(1, 10):
            ages[i - 1] = ages[i]
        ages[9] = 0
        print(sum(ages.values()))


if __name__ == '__main__':
    part_2()
