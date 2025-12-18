from common.solution import Solution


class Day(Solution):
    def parse_input(self, raw: str):
        return [x.split(":") for x in raw.strip().split('\n')]
    
    def parse_line(self, raw_line):
        """Parse a line into root and neighbors"""
        root = raw_line[0]
        rest = raw_line[1].strip().split(" ")
        return root, rest
    
    def create_adj_list(self):
        """Create adjacency list from input data"""
        d = {}
        for line in self.data:
            root, rest = self.parse_line(line)
            d.setdefault(root, []).extend(rest)
        return d
    
    def count_paths(self, start, end, special_nodes=None):
        """Count paths from start to end, tracking special nodes"""
        g = self.create_adj_list()
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
    
    def part1(self):
        """Count total paths from 'you' to 'out'"""
        start = "you"
        end = "out"
        total_paths, _ = self.count_paths(start, end)
        return total_paths
    
    def part2(self):
        """Count paths from 'svr' to 'out' visiting both 'dac' and 'fft'"""
        start = "svr"
        end = "out"
        special_nodes = ["dac", "fft"]
        _, paths_with_both = self.count_paths(start, end, special_nodes)
        return paths_with_both


Day().solve()
