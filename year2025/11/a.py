from linereader import read_file

data = [x.split(":") for x in read_file('test.input.txt')]


def parse_input(raw_line):
    root = raw_line[0]
    rest = raw_line[1]

    rest = rest.strip().split(" ")

    return root, rest

def create_adj_list():
    d = {}

    for line in data:
        root, rest = parse_input(line)

        d.setdefault(root, []).extend(rest)


    return d

g = create_adj_list()



