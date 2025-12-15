from linereader import read_file

data = [int(x) for x in read_file('1.input.txt')]

total_fuel = 0

for module_mass in data:
    fuel_weight = module_mass // 3 - 2
    total_fuel += fuel_weight

print(total_fuel)
