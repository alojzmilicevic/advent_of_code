from itertools import permutations
from common.solution import Solution
from common.grid_printer import print_table, Colors


class Day(Solution):
    def parse_data(self):
        cities = []
        seen = set()
        distances = {}
        for line in self.data:
            a, _, b, _, d = line.split(" ")

            if a not in seen:
                cities.append(a)
                seen.add(a)
            if b not in seen:
                cities.append(b)
                seen.add(b)

            distances[(a, b)] = int(d)
            distances[(b, a)] = int(d)
        return cities, distances

    def part1(self):
        cities, distances = self.parse_data()

        min_dist = float("inf")
        for route in permutations(cities):
            total = 0
            for i in range(len(route) - 1):
                total += distances[(route[i], route[i + 1])]
            min_dist = min(min_dist, total)

        return min_dist

    def part2(self):
        cities, distances = self.parse_data()

        max_dist = 0
        for route in permutations(cities):
            total = 0
            for i in range(len(route) - 1):
                total += distances[(route[i], route[i + 1])]
            max_dist = max(max_dist, total)

        return max_dist


Day().solve()
