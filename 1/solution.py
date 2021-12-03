import numpy as np

import utils.file_io


def part_1():
    data = utils.file_io.read_as_np_array('input.txt')
    print(np.where(data[1:] - data[:-1] > 0)[0].shape[0])

def part_2():
    data = utils.file_io.read_as_np_array('input.txt')
    slidings = data[:-2] + data[1:-1] + data[2:]
    print(np.where(slidings[1:] - slidings[:-1] > 0)[0].shape[0])


if __name__ == '__main__':
    part_1()
    part_2()