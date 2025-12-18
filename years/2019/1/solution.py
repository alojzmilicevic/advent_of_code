from common.solution import Solution


class Day(Solution):
    def parse_input(self, raw: str):
        return [int(x) for x in raw.strip().split("\n")]

    def part1(self):
        total_fuel = 0
        for module_mass in self.data:
            fuel_weight = module_mass // 3 - 2
            total_fuel += fuel_weight
        return total_fuel

    def part2(self):
        total_fuel = 0
        for module_mass in self.data:
            fuel_weight = module_mass
            while fuel_weight > 0:
                fuel_weight = fuel_weight // 3 - 2
                if fuel_weight > 0:
                    total_fuel += fuel_weight
        return total_fuel


Day().solve()
