from common.solution import Solution


class Day(Solution):
    def move(self, x, y, char):
        if char == '^':
            return x, y + 1
        elif char == 'v':
            return x, y - 1
        elif char == '>':
            return x + 1, y
        elif char == '<':
            return x - 1, y
        return x, y
    
    def part1(self):
        visited = {(0, 0)}
        x, y = 0, 0

        for char in self.raw_input:
            x, y = self.move(x, y, char)
            visited.add((x, y))
        return len(visited)
    
    def part2(self):
        visited = {(0, 0)}
        santa = [0, 0]
        robot = [0, 0]

        for i, char in enumerate(self.raw_input):
            pos = santa if i % 2 == 0 else robot
            pos[0], pos[1] = self.move(pos[0], pos[1], char)
            visited.add((pos[0], pos[1]))
        return len(visited)


Day().solve()
