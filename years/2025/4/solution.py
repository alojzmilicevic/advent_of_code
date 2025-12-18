from common.solution import Solution


class Day(Solution):
    def parse_input(self, raw: str):
        return [list(x) for x in raw.strip().split("\n")]

    def count_neighbors(self, x, y, grid):
        count = 0
        for i in range(x - 1, x + 2):
            if i < 0 or i >= len(grid):
                continue

            for j in range(y - 1, y + 2):
                if j < 0 or j >= len(grid[0]):
                    continue
                if j == y and i == x:
                    continue

                if grid[i][j] == "@":
                    count += 1

        return count

    def part1(self):
        count = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] == "@":
                    if self.count_neighbors(i, j, self.data) < 4:
                        count += 1
        return count

    def part2(self):
        data = [row[:] for row in self.data]

        total = 0
        while True:
            marked = []
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if data[i][j] == "@":
                        if self.count_neighbors(i, j, data) < 4:
                            marked.append((i, j))

            if not marked:
                break

            total += len(marked)
            for i, j in marked:
                data[i][j] = "."

        return total


Day().solve()
