from linereader import read_file

data = [int(x) for x in read_file('1.input.txt')]

total_fuel = 0

for module_mass in data:
    fuel_weight = module_mass

    while fuel_weight > 0:
        fuel_weight = fuel_weight // 3 - 2

        if fuel_weight > 0:
            total_fuel += fuel_weight

# Part 2 - Prints the total fuel
print(total_fuel)
