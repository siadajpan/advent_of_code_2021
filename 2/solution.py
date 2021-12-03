
import utils.file_io

DATA = utils.file_io.read_file('input.txt')


def part_1():
    hor = sum([int(el.split(' ')[1]) for el in DATA if el.split(' ')[0] == 'forward'])
    depth = sum([int(el.split(' ')[1]) for el in DATA if el.split(' ')[0] == 'down']) \
            - sum([int(el.split(' ')[1]) for el in DATA if el.split(' ')[0] == 'up'])
    print(hor, depth, hor * depth)


def part_2():
    hor = 0
    depth = 0
    aim = 0

    for command in DATA:
        c, n = command.split(' ')
        n = int(n)
        if c == 'down':
            aim += n
        elif c == 'up':
            aim -= n
        elif c == 'forward':
            hor += n
            depth += n * aim

    print(hor, depth, hor * depth)


if __name__ == '__main__':
    part_1()
    part_2()