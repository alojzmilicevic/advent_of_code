from intcode_computer.computer import Computer
from linereader import read_line

data = read_line('2.input.txt', ',')

# Part 1
data[1] = 12
data[2] = 2

data = [int(item) for item in data]
c = Computer(data.copy())
a = c.run([0])
print(a)
