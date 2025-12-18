from common.solution import Solution


class Day(Solution):
    def sim_good(self, fish, days):
        fish_age = {key: 0 for key in range(9)}
        for age in fish:
            fish_age[age] += 1
        
        for day in range(days):
            new_fish = fish_age[0]
            fish_age = {key - 1: value for (key, value) in fish_age.items() if key > 0}
            fish_age[6] = fish_age.get(6, 0) + new_fish
            fish_age[8] = new_fish
        return sum(fish_age.values())
    
    def part1(self):
        initial_state = [int(x) for x in self.data[0].split(',')]
        return self.sim_good(initial_state, 80)
    
    def part2(self):
        initial_state = [int(x) for x in self.data[0].split(',')]
        return self.sim_good(initial_state, 256)


Day().solve()
