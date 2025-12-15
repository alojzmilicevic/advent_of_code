from common.solution import Solution


class Day(Solution):
    def extract_dimensions(_, line):
        dimensions = line.split('x')
        l, w, h = map(int, dimensions)
        return sorted([l, w, h])

    def calc(self):
        total_package = 0
        total_ribbon = 0

        for line in self.data:  
            l, w, h = self.extract_dimensions(line)
            
            total_package += 2*l*w + 2*w*h + 2*h*l + l*w
            total_ribbon += 2*(l + w) + (l * w * h)
        return total_package, total_ribbon
    
    def part1(self):
        return self.calc()[0]

    def part2(self):
        return self.calc()[1]

Day(input_file="input.txt").solve()
