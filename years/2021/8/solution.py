from common.solution import Solution


class Day(Solution):
    def part1(self):
        d = [x.split('| ')[1].split(' ') for x in self.data]
        
        total = 0
        for line in d:
            for s in line:
                if len(s) == 2 or len(s) == 3 or len(s) == 4 or len(s) == 7:
                    total += 1
        
        return total
    
    def part2(self):
        # TODO: Need to implement part2 logic
        return 0


Day().solve()
