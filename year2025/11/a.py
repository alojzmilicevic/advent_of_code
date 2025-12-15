from linereader import read_file

def parse_input(raw_line):
    root = raw_line[0]
    rest = raw_line[1].strip().split(" ")
    return root, rest

def create_adj_list(file_name):
    data = [x.split(":") for x in read_file(file_name)]
    d = {}
    for line in data:
        root, rest = parse_input(line)
        d.setdefault(root, []).extend(rest)
    return d

def count_paths(start, end, file_name, special_nodes=None):
    g = create_adj_list(file_name)
    special_nodes = set(special_nodes) if special_nodes else set()
    memo = {}

    def dfs(node, num_special_visited=0):
        key = (node, num_special_visited)
        if key in memo:
            return memo[key]

        if node in special_nodes and num_special_visited < 2:
            num_special_visited += 1

        if node == end:
            total_paths = 1
            paths_with_special = 1 if num_special_visited == 2 else 0
            memo[key] = (total_paths, paths_with_special)
            return memo[key]

        total_paths = 0
        paths_with_special = 0
        for neighbor in g.get(node, []):
            t, s = dfs(neighbor, num_special_visited)
            total_paths += t
            paths_with_special += s

        memo[key] = (total_paths, paths_with_special)
        return memo[key]

    return dfs(start, 0)

# Part 1
start1 = "you"
end1 = "out"
total_paths1, _ = count_paths(start1, end1, "input.txt")
print("Part 1 total paths (you -> out):", total_paths1)

# Part 2
start2 = "svr"
end2 = "out"
special_nodes = ["dac", "fft"]
_, paths_with_both = count_paths(start2, end2, "input.txt", special_nodes)
print("Part 2 paths visiting both dac and fft:", paths_with_both)
