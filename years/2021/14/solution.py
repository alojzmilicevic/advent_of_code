from common.solution import Solution
from collections import defaultdict, Counter


class Day(Solution):
    def parse_polymer_input(self):
        # Split into start and rules
        start = None
        rules_data = []
        
        reading_rules = False
        for line in self.data:
            if not line.strip():
                reading_rules = True
                continue
            
            if reading_rules:
                rules_data.append(line)
            else:
                start = line
        
        rules = dict([(p[0], p[1]) for p in [y.replace(' -> ', ' ').split(' ') for y in rules_data]])
        
        return start, rules
    
    def simulate(self, steps):
        start, rules = self.parse_polymer_input()
        
        pairs = Counter(start[i: i + 2] for i in range(len(start) - 1))
        char_count = Counter(start)
        
        for i in range(steps):
            new_pairs = defaultdict(int)
            for pair, cur_count in pairs.items():
                if pair in rules:
                    c = rules[pair]
                    new_pairs[pair[0] + c] += cur_count
                    new_pairs[c + pair[1]] += cur_count
                    char_count[c] += cur_count
            
            pairs = new_pairs
        
        return max(char_count.values()) - min(char_count.values())
    
    def part1(self):
        return self.simulate(10)
    
    def part2(self):
        return self.simulate(40)


Day().solve()
