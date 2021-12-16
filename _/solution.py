# DATA = utils.file_io.read_file('input_ex.txt')


def to_bin(data):
    binary = ''.join([f'{(int(f"0x{e}", 16)):04b}' for e in data])
    return binary


def packets(data):
    number = ''
    for i in range(100):
        d = data[i * 5: (i + 1) * 5]
        number += str(d[1:])
        if d[0] == '0':
            break
    number = int(number, 2)
    return number

def literal(data):
    data_l = data[6:]
    return packets(data_l)

def operator(data):
    length_type_id = data[6]
    if length_type_id == 0:
        length = int(data[7:7+15], 2)

    elif length_type_id == 1:
        length = int(data[7:7+11], 2)

def read_version(data):
    packet_v = int(data[:3], 2)
    return packet_v


def read_type_id(data):
    type_id = int(data[3:6], 2)
    return type_id


def part_1(data):
    b = to_bin(data)
    v, t = read_version(b), read_type_id(b)
    print(v, t)
    if t == 4:
        number = literal(b)
        print(number)
    else:
        op = operator(b)
        print(op)

def part_2():
    pass


if __name__ == '__main__':
    for data in ['D2FE28', '38006F45291200']:
        part_1(data)
