import numpy as np

import utils.file_io

DATA = utils.file_io.read_file('input.txt')


def output_pixel(image, pos, algo, space):
    i, j = pos
    res = ''
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            ni, nj = i + di, j + dj
            if ni not in range(len(image)) or nj not in range(len(image[0])):
                res += space
            else:
                res += image[ni][nj]
    idx = int(res, 2)
    return algo[idx]


def get_output(image, algo, space='0'):
    count = 0
    new_image = []

    for i in range(-1, len(image) + 1):
        row = ''
        for j in range(-1, len(image[0]) + 1):
            pixel = output_pixel(image, (i, j), algo, space)
            if pixel == '1':
                count += 1
            row += pixel
        new_image.append(row)
    space = output_pixel(image, (-2, -2), algo, space)
    return new_image, count, space


def part_1(image, algo):
    space = '0'

    for i in range(2):
        image, count, space = get_output(image, algo, space)
        print(image)
        print(i, count)



def part_2(image, algo):
    space = '0'

    for i in range(50):
        image, count, space = get_output(image, algo, space)
        print(image)
        print(i, count)


if __name__ == '__main__':
    DATA = [D.replace('.', '0').replace('#', '1') for D in DATA]
    print(DATA)
    arr = DATA[0]
    image = np.array([[d_ for d_ in d] for d in DATA[2:]], dtype=str)
    print(image)
    # part_1(image, arr)
    part_2(image, arr)
