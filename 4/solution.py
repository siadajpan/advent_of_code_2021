import re

import numpy as np

import utils.file_io


def part_1():
    def check_win(boards):
        ax0 = np.sum(boards, axis=1)
        ax1 = np.sum(boards, axis=2)
        if not np.all(ax0 * ax1):
            print(ax0 * ax1)
            print(np.where(ax0 * ax1 == 0))
            return np.where(ax0 * ax1 == 0)[0][0]
        return None

    data = utils.file_io.read_file('input.txt')
    print(data)
    numbers = np.array(re.findall(r'[\d]+', data[0]), dtype=int)
    print(numbers)
    boards = data[2:]
    boards = np.array([np.array([re.findall(r'[\d]+', b) for b in boards[i*6:(i*6+5)]]) for i in range(int(len(boards)/6)+1)], dtype=int)
    boards[np.where(boards==0)] = 100

    for number in numbers:
        if number == 0:
            number = 100
        print('number', number)
        boards[np.where(boards == number)] = 0
        if check_win(boards) is not None:
            break
    boards[np.where(boards == 100)] = 0
    print(boards)
    s =np.sum(boards[check_win(boards)])
    print('res', s, number,s * number )


def part_2():
    def check_win(boards, last_boards):
        ax0 = np.sum(boards, axis=1)
        ax1 = np.sum(boards, axis=2)
        print(ax0 * ax1)
        print('prod', np.prod(ax0 * ax1, axis=1))

        if not np.any(np.prod(ax0 * ax1, axis=1)):
            ax0 = np.sum(last_boards, axis=1)
            ax1 = np.sum(last_boards, axis=2)
            return np.where(np.prod(ax0 * ax1, axis=1) != 0)[0][0]
        return None

    data = utils.file_io.read_file('input.txt')
    print(data)
    numbers = np.array(re.findall(r'[\d]+', data[0]), dtype=int)
    print(numbers)
    boards = data[2:]
    boards = np.array([np.array([re.findall(r'[\d]+', b) for b in boards[i*6:(i*6+5)]]) for i in range(int(len(boards)/6)+1)], dtype=int)
    boards[np.where(boards==0)] = 100

    for number in numbers:
        if number == 0:
            number = 100
        print('number', number)
        last_boards = boards.copy()
        boards[np.where(boards == number)] = 0
        if check_win(boards, last_boards) is not None:
            break
    boards[np.where(boards == 100)] = 0
    print(boards)
    s =np.sum(boards[check_win(boards, last_boards)])
    print('res', s, number,s * number )



if __name__ == '__main__':
    part_2()