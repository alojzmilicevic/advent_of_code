from common.solution import Solution
from lib.point2d import Point2D


class Day(Solution):
    def parse_input(self, raw: str):
        return [Point2D(*map(int, x.split(","))) for x in raw.strip().split("\n")]

    def part1(self):
        points = self.data
        max_area = 0

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                a = points[i]
                b = points[j]
                dx = abs(a.x - b.x) + 1
                dy = abs(a.y - b.y) + 1
                if dx * dy > max_area:
                    max_area = dx * dy

        return max_area

    def part2(self):
        points = [(p.y, p.x) for p in self.data]

        points_x, points_y = set(), set()
        for x, y in points:
            points_x.update((x - 1, x, x + 1))
            points_y.update((y - 1, y, y + 1))

        compressed_x = {x: i for i, x in enumerate(sorted(points_x))}
        compressed_y = {y: i for i, y in enumerate(sorted(points_y))}

        n, m = len(compressed_x), len(compressed_y)
        grid = [[-1] * m for _ in range(n)]

        for i in range(len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]

            x1, y1 = compressed_x[x1], compressed_y[y1]
            x2, y2 = compressed_x[x2], compressed_y[y2]

            if x1 == x2:
                for j in range(min(y1, y2), max(y1, y2) + 1):
                    grid[x1][j] = 1
            else:
                for j in range(min(x1, x2), max(x1, x2) + 1):
                    grid[j][y1] = 1

        stack = [(0, 0)]
        grid[0][0] = 0
        while stack:
            x, y = stack.pop()
            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == -1:
                    stack.append((nx, ny))
                    grid[nx][ny] = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == -1:
                    grid[i][j] = 1

        prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                prefix_sum[i + 1][j + 1] = (
                    grid[i][j]
                    + prefix_sum[i][j + 1]
                    + prefix_sum[i + 1][j]
                    - prefix_sum[i][j]
                )

        ans = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                x1, y1 = min(p1[0], p2[0]), min(p1[1], p2[1])
                x2, y2 = max(p1[0], p2[0]), max(p1[1], p2[1])

                cx1, cy1 = compressed_x[x1], compressed_y[y1]
                cx2, cy2 = compressed_x[x2], compressed_y[y2]

                rect_sum = (
                    prefix_sum[cx2 + 1][cy2 + 1]
                    - prefix_sum[cx1][cy2 + 1]
                    - prefix_sum[cx2 + 1][cy1]
                    + prefix_sum[cx1][cy1]
                )
                if rect_sum == (cx2 - cx1 + 1) * (cy2 - cy1 + 1):
                    area = (x2 - x1 + 1) * (y2 - y1 + 1)
                    ans = max(ans, area)

        return ans


Day().solve()
