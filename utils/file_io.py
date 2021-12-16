import os
import urllib.request

import numpy as np


def read_file(file_path):
    with open(file_path) as file:
        data = file.read().splitlines()

    if data[-1] == '':
        data = data[:-1]

    return data


def read_as_np_array(file_path, dtype=np.int, digits=False):
    data = read_file(file_path)
    if data[-1] == '':
        data = data[:-1]
    if digits:
        data = [[el for el in row] for row in data]

    return np.asarray(data, dtype=dtype)


if __name__ == '__main__':
    data = read_as_np_array('/home/karol/projects/advent_of_code_2021/3/input_ex.txt')
    print(data)