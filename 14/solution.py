import re

import numpy as np

import utils.file_io

DATA = utils.file_io.read_file('input.txt')
TEMPLATE = DATA[0]
INS = []
for d in DATA[2:]:
    pair, insertion = re.match(r'([\w]+) -> (\w)', d).groups()
    INS.append((pair, insertion))
print(TEMPLATE, INS)

def part_1():
    polymers = TEMPLATE
    for _ in range(40):
        print(_)
        for p, i in INS:
            # print(f'before {p}->{i} {polymers}')
            polymers = polymers.replace(p, p[0]+i.lower()+p[1]).replace(p, p[0]+i.lower()+p[1])
            # print('after', polymers)
        polymers = polymers.upper()
        # print(polymers, '\n')
    counts = [polymers.count(letter) for letter in ['N', 'C', 'B', 'H']]
    print(max(counts), min(counts), max(counts) - min(counts))


def part_2():
    pairs = {}
    for i in range(len(TEMPLATE) - 1):
        pairs[TEMPLATE[i: i+2]] = {'count': 1, 'update': None}
    # print(pairs)
    for _ in range(40):
        print(_)
        for p, i in INS:
            if p not in pairs.keys():
                continue
            pairs[p]['update'] = i
        # print('before update', pairs)
        new_pairs = {}
        for name, data in pairs.items():
            if data['update'] is None:
                continue
            for pair in [name[0] + data['update'], data['update'] + name[1]]:
                if pair in new_pairs.keys():
                    new_pairs[pair]['count'] += data['count']
                else:
                    new_pairs[pair] = {'count': data['count'], 'update': None}
            pairs[name]['update'] = None
            pairs[name]['count'] = 0
        # print('before', pairs)
        # print('new pairs', new_pairs)
        for name in list(pairs.keys()):
            if pairs[name]['count'] == 0:
                del pairs[name]
        for new_name, data in new_pairs.items():
            if new_name in pairs.keys():
                pairs[new_name]['count'] += data['count']
            else:
                pairs[new_name] = data

        # print('after', pairs)

    print(pairs)
    # polymers = ' '.join([p * i['count'] for p, i in pairs.items()]) + TEMPLATE[0] + TEMPLATE[-1]
    # print(len(polymers)/2)
    # print(polymers)
    letters = {}
    for n, data in pairs.items():
        for letter in n:
            if letter in letters.keys():
                letters[letter] += data['count']
            else:
                letters[letter] = data['count']
    for letter in [TEMPLATE[0], TEMPLATE[-1]]:
        letters[letter] += 1
    counts = list(letters.values())
    print(max(counts)/2, min(counts)/2, max(counts)/2 - min(counts)/2)


if __name__ == '__main__':
    part_2()
