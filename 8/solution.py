import numpy as np

import utils.file_io

DATA = utils.file_io.read_file('input.txt')

DATA_IN, DATA_OUT = [], []
for d in DATA:
    d_in, d_out = d.split(' | ')
    d_in, d_out = [d.split(' ') for d in [d_in, d_out]]
    DATA_IN.append(d_in)
    DATA_OUT.append(d_out)

DATA = np.array(DATA)


def part_1():
    small_numbers = 0
    for d in DATA_OUT:
        small_numbers += len([n for n in d if len(n) in [2, 3, 4, 7]])
    print(small_numbers)


def part_2():
    def _data_to_dict(full_data):
        dicts = []
        for data in full_data:
            digits_dict = {}
            for digit in data:
                len_ex = digits_dict.get(len(digit))
                if len_ex is None:
                    digits_dict[len(digit)] = []
                digits_dict[len(digit)].append(digit)
            dicts.append(digits_dict)
        return dicts

    def find_places(digit_dict):
        # print('dd', digit_dict)
        one = digit_dict[2][0]
        top = [el for el in digit_dict[3][0] if el not in digit_dict[2][0]][0]
        top_mid_bottom = [el for el in digit_dict[5][0] if el in digit_dict[5][1] and el in digit_dict[5][2]]
        # print('tmb', top_mid_bottom)
        mid = [el for el in top_mid_bottom if el in digit_dict[4][0]][0]
        # print('mid', mid)
        left_top = [el for el in digit_dict[4][0] if el not in top_mid_bottom and el not in digit_dict[2][0]][0]
        bottom = [el for el in top_mid_bottom if el not in [top, mid]][0]
        five = [el for el in digit_dict[5] if left_top in el][0]
        right_bottom = [el for el in five if el not in [*top_mid_bottom, left_top]][0]
        right_top = [el for el in one if el != right_bottom][0]
        left_bottom = \
        [el for el in digit_dict[7][0] if el not in [top, mid, bottom, left_top, right_top, right_bottom]][0]

        return {
            top: 't',
            mid: 'm',
            bottom: 'b',
            left_top: 'lt',
            left_bottom: 'lb',
            right_top: 'rt',
            right_bottom: 'rb'
        }

    def find_number(digits, digit_places):
        NUMBERS = {
            0: ['t', 'b', 'lt', 'lb', 'rt', 'rb'],
            1: ['rt', 'rb'],
            2: ['t', 'm', 'b', 'rt', 'lb'],
            3: ['t', 'm', 'b', 'rt', 'rb'],
            4: ['lt', 'm', 'rt', 'rb'],
            5: ['t', 'm', 'b', 'lt', 'rb'],
            6: ['t', 'm', 'b', 'lt', 'lb', 'rb'],
            7: ['t', 'rt', 'rb'],
            8: ['t', 'm', 'b', 'lt', 'lb', 'rt', 'rb'],
            9: ['t', 'm', 'b', 'lt', 'rt', 'rb']
        }
        # print('digits', digits, 'places', digit_places)
        place = [digit_places[d] for d in digits]
        # print('place', place)
        for value, n in NUMBERS.items():
            # print('checking ', value, n, len([p for p in place if p in n]) == len(place) and len(place) == len(n))
            if len([p for p in place if p in n]) == len(place) and len(place) == len(n):
                return value

    dd = _data_to_dict(DATA_IN)
    num_out = []
    for d, data_out in zip(dd, DATA_OUT):
        places = find_places(d)
        # print(places)
        # print(d)
        numbers = [str(find_number(do, places)) for do in data_out]
        num_out.append(int(''.join(numbers)))
    print(sum(num_out))
        # print(data_out)
        # print(numbers)



if __name__ == '__main__':
    part_2()
