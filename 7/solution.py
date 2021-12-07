import numpy as np

import utils.file_io

DATA = [int(a) for a in utils.file_io.read_file('input.txt')[0].split(',')]
DATA = np.array(DATA)


def part_1():
    print(np.median(DATA))
    s = sum(abs(DATA - int(np.median(DATA))))
    print(s)


def part_2():
    def fuel_cost(pos, end):
        int((abs(pos - end) + 1) / 2 * abs(pos - end))

    costs = min([sum([fuel_cost(pos, end) for pos in DATA])
                 for end in range(max(DATA))])

    print(costs)


if __name__ == '__main__':
    part_2()
