import utils.file_io

DATA = utils.file_io.read_file('input.txt')


class NodeP1:
    def __init__(self, name: str, outs=None):
        self.name = name
        self.outs = outs if outs is not None else []
        self.big = name.isupper()
        print(f'name {name} {name.isupper()}, big {self.big}')

    def go(self, current_path, all_paths):
        if self.name == 'end':
            print(f'We are at the end with {current_path}')
            all_paths.append(current_path)
            return

        for out in self.outs:
            print(f'going from {self.name} to {out.name}')
            if not out.big and out in current_path:
                print(f'{out} is big {out.big}')
                continue
            new_path = current_path.copy()
            new_path.append(out)
            print('current path', new_path)
            out.go(new_path, all_paths)

    def __repr__(self):
        return self.name


class NodeP2:
    def __init__(self, name: str, outs=None):
        self.name = name
        self.outs = outs if outs is not None else []
        self.big = name.isupper()
        self.visited = 0
        print(f'name {name} {name.isupper()}, big {self.big}')

    def visited_twice(self, path):
        names = [n.name for n in path if not n.big and n not in ['start', 'stop']]
        return len(names) != len(set(names))

    def go(self, current_path, all_paths):
        if self.name == 'end':
            print(f'We are at the end with {current_path}')
            all_paths.append(current_path)
            return

        for out in self.outs:
            print(f'going from {self.name} to {out.name}')
            if not out.big and out in current_path and self.visited_twice(current_path):
                continue
            if out.name == 'start':
                continue
            new_path = current_path.copy()
            new_path.append(out)
            print('current path', new_path)
            out.go(new_path, all_paths)

    def __repr__(self):
        return self.name


NODES_P1 = []
for d in DATA:
    connection = d.split('-')
    for c in connection:
        if c not in [n.name for n in NODES_P1]:
            NODES_P1.append(NodeP1(c))
    node0 = [n for n in NODES_P1 if n.name == connection[0]][0]
    node1 = [n for n in NODES_P1 if n.name == connection[1]][0]
    node0.outs.append(node1)
    node1.outs.append(node0)

NODES_P2 = []
for d in DATA:
    connection = d.split('-')
    for c in connection:
        if c not in [n.name for n in NODES_P2]:
            NODES_P2.append(NodeP2(c))
    node0 = [n for n in NODES_P2 if n.name == connection[0]][0]
    node1 = [n for n in NODES_P2 if n.name == connection[1]][0]
    node0.outs.append(node1)
    node1.outs.append(node0)


# NP_DATA = utils.file_io.read_as_np_array('input.txt')
# DATA = np.array(DATA)


def part_1():
    start_node = [n for n in NODES_P1 if n.name == 'start'][0]
    print(start_node)
    print(DATA)
    print(NODES_P1)
    all_paths = []
    print(start_node.go([start_node], all_paths))
    print(all_paths)
    print(len(all_paths))


def part_2():
    start_node = [n for n in NODES_P2 if n.name == 'start'][0]
    print(start_node)
    print(DATA)
    print(NODES_P1)
    all_paths = []
    print(start_node.go([start_node], all_paths))
    print(all_paths)
    print(len(all_paths))


if __name__ == '__main__':
    part_2()
