from itertools import permutations
from common.solution import Solution
import re


class Day(Solution):
    def parse_relationships(self):
        guests = set()
        happiness = {}

        for line in self.data:
            match = re.match(r"(\w+) would (gain|lose) (\d+) .* (\w+)\.$", line)
            person_a, sign, amount, person_b = match.groups()
            guests.update([person_a, person_b])

            amount = int(amount) if sign == "gain" else -int(amount)
            happiness[(person_a, person_b)] = amount

        return guests, happiness

    def calculate_best_happiness(self, guests_set, happiness):
        guests = sorted(guests_set)
        max_happiness = 0

        for perm in permutations(guests[1:]):
            total = 0
            arrangement = (guests[0],) + perm
            for i in range(len(arrangement)):
                a = arrangement[i]
                b = arrangement[(i + 1) % len(arrangement)]

                # Add happiness for both directions (a->b and b->a)
                total += happiness.get((a, b), 0)
                total += happiness.get((b, a), 0)

            max_happiness = max(total, max_happiness)

        return max_happiness

    def part1(self):
        guests, happiness = self.parse_relationships()
        return self.calculate_best_happiness(guests, happiness)

    def part2(self):
        guests, happiness = self.parse_relationships()

        guests.add("Me")
        for guest in guests:
            if guest != "Me":
                happiness[("Me", guest)] = 0
                happiness[(guest, "Me")] = 0

        return self.calculate_best_happiness(guests, happiness)


Day().solve()
