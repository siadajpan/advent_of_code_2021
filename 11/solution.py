import numpy as np

import utils.file_io

NP_DATA = utils.file_io.read_as_np_array('input.txt', digits=True)


def part_1(data=NP_DATA, part_2=False):
    def _update_flash(table):
        flash = np.where(table >= 10)
        print('for update', flash)
        y_max, x_max = table.shape
        for y, x in zip(*flash):
            # print(x, y)
            table[y, x] = -10
            for x_ in range(x - 1, x + 2):
                if x_ < 0 or x_ >= x_max:
                    continue
                for y_ in range(y - 1, y + 2):
                    if y_ < 0 or y_ >= y_max:
                        continue
                    # print('updating', x_, y_)
                    table[y_, x_] += 1
        return table

    print(data)
    flashes = 0
    i_range = 1000 if part_2 else 100

    for i in range(i_range):
        data += 1
        print('data before update\n', data)
        old_data = data.copy()
        data = _update_flash(data)
        while not np.array_equal(old_data, data):
            print('updating ')
            old_data = data.copy()
            print('before update\n', old_data)
            data = _update_flash(old_data.copy())
        data[np.where(data < 0)] = 0
        flashes += len(np.where(data == 0)[0])
        if part_2:
            if len(np.where(data == 0)[0]) == 100:
                print(f'synchronized flash: {i}')
                break
        print('after update\n', data)
        print('arrays equal', np.array_equal(old_data, data), '\n\n', old_data, '\n\n', data)
        print('flashes', flashes)


def part_2():
    part_1(part_2=True)


if __name__ == '__main__':
    part_2()
