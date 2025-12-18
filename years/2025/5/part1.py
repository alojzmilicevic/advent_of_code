from common.solution import Solution
import sys


class Day(Solution):
    def parse_input(self, raw: str):
        """Parse the input into ranges and ingredient IDs"""
        parts = raw.strip().split("\n\n")

        # Parse fresh ID ranges
        ranges = []
        for line in parts[0].split("\n"):
            start, end = map(int, line.split("-"))
            ranges.append((start, end))

        # Parse available ingredient IDs
        ingredient_ids = []
        if len(parts) > 1:
            for line in parts[1].split("\n"):
                if line.strip():
                    ingredient_ids.append(int(line))

        return ranges, ingredient_ids

    def is_fresh(self, ingredient_id, ranges):
        """Check if an ingredient ID is fresh (falls in any range)"""
        for start, end in ranges:
            if start <= ingredient_id <= end:
                return True
        return False

    def merge_intervals(self, intervals):
        """Merge overlapping intervals"""
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_start, last_end = merged[-1]

            if start <= last_end + 1:  # +1 to merge adjacent ranges
                merged[-1] = (last_start, max(last_end, end))
            else:
                merged.append((start, end))

        return merged

    def part1(self):
        """Count how many available ingredient IDs are fresh"""
        ranges, ingredient_ids = self.data

        count = 0
        for ingredient_id in ingredient_ids:
            if self.is_fresh(ingredient_id, ranges):
                count += 1

        return count

    def part2(self):
        """Count total coverage of merged intervals"""
        ranges, ingredient_ids = self.data

        merged = self.merge_intervals(ranges)

        total = 0
        for start, end in merged:
            total += end - start + 1

        return total


Day().solve()
