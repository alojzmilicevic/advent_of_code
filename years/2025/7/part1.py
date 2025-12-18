from common.solution import Solution


class Day(Solution):
    def parse_input(self, raw: str):
        return [x for x in raw.strip().split("\n")]

    def part1(self):
        """Count number of splits ('^' cells)"""
        grid = self.data
        H = len(grid)
        W = len(grid[0])

        # Find S
        start_row = 0
        start_col = grid[0].index("S")

        queue = [(start_row, start_col)]
        visited = set()
        splits = 0

        while queue:
            r, c = queue.pop(0)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            cell = grid[r][c]

            if cell == "^":
                splits += 1

                if c - 1 >= 0:
                    queue.append((r, c - 1))
                if c + 1 < W:
                    queue.append((r, c + 1))

                # Do not continue downwards from a split
                continue

            if r + 1 < H:
                queue.append((r + 1, c))  # down

        return splits

    def part2(self):
        """Count total timelines (paths from S to bottom row)"""
        grid = self.data
        H = len(grid)
        W = len(grid[0])

        # Find S
        start_row = 0
        start_col = grid[0].index("S")

        ways = [[0] * W for _ in range(H)]
        ways[start_row][start_col] = 1

        for r in range(H):
            for c in range(W):
                if ways[r][c] == 0:
                    continue

                cell = grid[r][c]

                if cell in (".", "S"):
                    if r + 1 < H:
                        ways[r + 1][c] += ways[r][c]

                elif cell == "^":
                    if r + 1 < H:
                        if c - 1 >= 0:
                            ways[r + 1][c - 1] += ways[r][c]
                        if c + 1 < W:
                            ways[r + 1][c + 1] += ways[r][c]

        total_timelines = sum(ways[-1])
        return total_timelines


Day().solve()
