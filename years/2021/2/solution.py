from common.solution import Solution


class Day(Solution):
    def part1(self):
        y = 0
        x = 0
        
        for line in self.data:
            direction, delta = line.split(" ")
            delta = int(delta)
            
            if direction == "up":
                y -= delta
            elif direction == "down":
                y += delta
            elif direction == "forward":
                x += delta
        
        return x * y
    
    def part2(self):
        y = 0
        x = 0
        aim = 0
        
        for line in self.data:
            direction, delta = line.split(" ")
            delta = int(delta)
            
            if direction == "up":
                aim -= delta
            elif direction == "down":
                aim += delta
            elif direction == "forward":
                x += delta
                y += aim * delta
        
        return x * y


Day().solve()
