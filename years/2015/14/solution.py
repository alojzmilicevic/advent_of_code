from turtle import position
from common.solution import Solution
import re

pattern = re.compile(r"^\w+|\d+")


class Day(Solution):
    def get_distance_from_time(self, n, v, flight_time, rest_time):
        cycle_time = rest_time + flight_time
        full_cycles = n // cycle_time
        remainder = n % cycle_time

        distance = v * full_cycles * flight_time
        distance += v * min(remainder, flight_time)

        return distance

    def get_positions_after_n(self, n):
        positions = []
        for line in self.data:
            deer, v, flight_time, rest_time = pattern.findall(line)

            d = self.get_distance_from_time(n, int(v), int(flight_time), int(rest_time))

            positions.append((d, deer))

        return positions

    def part1(self):
        n = 2503

        positions = self.get_positions_after_n(n)

        return max(positions)

    def part2(self):
        n = 2503

        scores = {}

        for i in range(1, n + 1):
            positions = self.get_positions_after_n(i)

            max_distance = max(pos[0] for pos in positions)

            for distance, deer_name in positions:
                if deer_name not in scores:
                    scores[deer_name] = 0
                if distance == max_distance:
                    scores[deer_name] += 1

        return max(scores.values())


Day().solve()
