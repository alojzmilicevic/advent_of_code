from linereader import read_file

data = [x for x in read_file('input.txt')]

elf_calories = []
cur_cal = 0
for i in range(0, len(data)):
    if data[i] == '':
        elf_calories.append(cur_cal)
        cur_cal = 0
    else:
        cal = int(data[i])
        cur_cal += cal

sorted_elf_calories = sorted(elf_calories, reverse=True)
# Part 1
print(sorted_elf_calories[0])
# Part 2
print(sorted_elf_calories[0] + sorted_elf_calories[1] + sorted_elf_calories[2])
