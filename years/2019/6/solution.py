from common.solution import Solution


class Day(Solution):
    def parse_input(self, raw: str):
        orbits = {}
        for line in raw.strip().split('\n'):
            center, orbiter = line.split(')')
            orbits[orbiter] = center
        return orbits
    
    def path_to_com(self, planet, n=0, target='COM'):
        if planet == target:
            return n
        return self.path_to_com(self.data[planet], n + 1, target)
    
    def part1(self):
        total = 0
        for planet in self.data:
            total += self.path_to_com(planet)
        return total
    
    def part2(self):
        me = 'YOU'
        santa = 'SAN'
        
        santa_len = self.path_to_com(santa)
        my_len = self.path_to_com(me)
        
        x = -2
        
        for i in range(max(santa_len, my_len)):
            if me == santa:
                break
            
            if santa_len > my_len:
                santa = self.data[santa]
                santa_len -= 1
                x += 1
            elif my_len > santa_len:
                me = self.data[me]
                my_len -= 1
                x += 1
            else:
                me = self.data[me]
                santa = self.data[santa]
                x += 2
        
        return x


Day().solve()
