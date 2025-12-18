from common.solution import Solution


class Day(Solution):
    def parse_input(self, raw: str):
        return raw.strip().split('\n')
    
    def parse_line(self, line):
        """Parse a line to extract dimensions and values"""
        cleaned = line.replace('x', ' ').replace(':', '')
        return [int(n) for n in cleaned.split()]

    def fits_in_area(self, row):
        """Check if values fit in the area (width x height)"""
        width = row[0]
        height = row[1]
        values = row[2:]
        
        area = width * height
        total = sum(values) * 9
        
        return total <= area
    
    def run(self):
        """Single part - count rows that fit"""
        count = 0
        
        for line in self.data:
            if 'x' not in line:
                continue
                
            row = self.parse_line(line)
                
            if self.fits_in_area(row):
                count += 1
        
        return count


Day().solve()
