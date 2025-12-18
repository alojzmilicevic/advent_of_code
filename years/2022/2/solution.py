from common.solution import Solution


class Day(Solution):
    def part1(self):
        points = {
            "A": 1, "B": 2, "C": 3,
            "X": 1, "Y": 2, "Z": 3,
        }
        
        total = 0
        for line in self.data:
            a = points[line[0]]
            b = points[line[2]]
            
            total += b
            
            if a == b:
                total += 3
            else:
                comp = b - 1
                if comp == 0:
                    comp = 3
                if comp == a:
                    total += 6
        
        return total
    
    def part2(self):
        points = {
            "A": 1, "B": 2, "C": 3,
            "X": 1, "Y": 2, "Z": 3,
        }
        
        def loose(x):
            if x == 1:
                return 3
            elif x == 2:
                return 1
            return 2
        
        total = 0
        for line in self.data:
            a = points[line[0]]
            b = points[line[2]]
            
            if b == 1:
                total += loose(a)
            if b == 2:
                total += a
                total += 3
            if b == 3:
                total += ((a % 3) + 3) % 3 + 1
                total += 6
        
        return total


Day().solve()
