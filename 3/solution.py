import numpy as np

import utils.file_io


def _bit_to_number(bit_array):
    number = 0
    for bit in bit_array:
        number = (number << 1) | bit
    return number


def part_1():
    data = utils.file_io.read_as_np_array('input_ex.txt', digits=True)
    means_values = np.sum(data, axis=0) / data.shape[0]
    maxes = _bit_to_number(means_values > 0.5)
    mins = _bit_to_number(means_values < 0.5)

    print(maxes, mins, maxes * mins)


def part_2():
    data = utils.file_io.read_as_np_array('input.txt', digits=True)
    results = []
    for search in ['min', 'max']:
        data_left = data.copy()
        for index in range(data_left.shape[1]):
            means_values = np.sum(data_left[:, index], axis=0) / data_left.shape[0]
            search_bit = means_values >= 0.5 if search == 'max' else means_values < 0.5
            data_left = data_left[np.where(data_left[:, index] == search_bit)]
            if data_left.shape[0] == 1:
                print(f'result {search}: {data_left}, {_bit_to_number(data_left[0])}')
                results.append(_bit_to_number(data_left[0]))
                break
    print(f'final result = {results[0] * results[1]}')


if __name__ == '__main__':
    part_1()
    part_2()
