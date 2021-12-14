import re

import numpy as np

import utils.file_io

DATA = utils.file_io.read_file('input.txt')
data = []
folds = []
for d in DATA:
    if ',' in d:
        data.append(re.match(r'([\d]+),([\d]+)', d).groups())
    elif 'fold' in d:
        folds.append(re.match(r'fold along (\w)=([\d]+)', d).groups())
data = np.array(data, dtype=int)
folds = [(i, int(n)) for (i, n) in folds]
DATA = np.array(DATA)


def part_1():
    w, h = np.max(data + 1, axis=0)
    paper = np.zeros((h, w), dtype=int)
    paper[data[:, 1], data[:, 0]] = 1
    print(paper)
    i = 0
    for dir, value in folds:
        # print(dir, value)
        if dir == 'x':
            # print('paper before\n', paper)
            folded_array = paper[:, value + 1:]
            # print('fold before\n', folded_array)
            folded_array = np.flip(folded_array, 1)
            # print('fold after\n', folded_array)
            paper = paper[:, :value]
            if paper.shape[1] < folded_array.shape[1]:
                folded_array[:, -(paper.shape[1]):] += paper
                paper = folded_array
            else:
                paper[:, -(folded_array.shape[1]):] += folded_array
            # print('paper after\n', paper)
        if dir == 'y':
            folded_array = paper[value + 1:]
            # print('before\n', folded_array)
            folded_array = np.flip(folded_array, 0)
            # print('after\n', folded_array)
            paper = paper[:value]
            if paper.shape[0] < folded_array.shape[0]:
                folded_array[-(paper.shape[0]):] += paper
                paper = folded_array
            else:
                paper[-(folded_array.shape[0]):] += folded_array
            # print('paper after\n', paper)
        if i == 0:
            print(np.count_nonzero(paper))
        i += 1

    return paper


def part_2():
    paper = part_1()
    for row in paper:
        row = [(' ', '#')[int(el)] for el in row > 0]
        print(''.join(row))


if __name__ == '__main__':
    part_2()
