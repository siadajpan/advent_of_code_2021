import re

import numpy as np

import utils.file_io

DATA = utils.file_io.read_file('input.txt')

OPEN = ['(', '[', '{', '<']
CLOSE = [')', ']', '}', '>']

def part_1():
    points = [3, 57, 1197, 25137]
    incorrect = [o + c for o in OPEN for c in CLOSE
                 if OPEN.index(o) != CLOSE.index(c)]
    correct = [o + c for o, c in zip(OPEN, CLOSE)]
    print(incorrect)
    print(correct)
    print(DATA)
    error = False
    score = 0
    incomplete = []
    for d in DATA:
        print('\n\nd', d)
        old_d = ''
        error = False
        while old_d != d:
            old_d = d
            for c in correct:
                print('c', c)
                d = d.replace(c, '')
                print('after', d)
        # print('end', d)
        for i in incorrect:
            if i in d:
                print('incorrect', i, d)
                score += points[CLOSE.index(i[1])]
                print('score', score)
                error = True
                break
        if not error:
            print('unfinished', d)
            incomplete.append(d)
        # else:
        #     break

    return incomplete


def part_2():
    points = [1, 2, 3, 4]
    incomplete = part_1()
    print(incomplete)
    scores = []
    for el in incomplete:
        score = 0
        r = el[::-1]
        for open in r:
            score *= 5
            score += points[OPEN.index(open)]
            print('open', open, 'score', score)
        scores.append(score)
        print(r)

    print('result', sorted(scores)[int(len(scores)/2)])


if __name__ == '__main__':
    part_2()
