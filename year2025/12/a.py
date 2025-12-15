from linereader import read_file


def parse_line(line):
    cleaned = line.replace('x', ' ').replace(':', '')
    return [int(n) for n in cleaned.split()]


def fits_in_area(row):
    width = row[0]
    height = row[1]
    values = row[2:]
    
    area = width * height
    total = sum(values) * 9
    
    return total <= area


count = 0
    
for line in read_file('input.txt'):
    if 'x' not in line:
        continue
        
    row = parse_line(line)
        
    if fits_in_area(row):
        count += 1
    
print(count)


