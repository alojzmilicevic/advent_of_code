from linereader import read_line
from intcode_computer.computer import Computer

data = [int(x) for x in read_line('5.input.txt', ',')]

print("Running tests, no output means everything is OK...")

test_a = Computer(data.copy())

for i in range(0, 9):
    if i == 0:
        test_a.run([1, 1])
    else:
        test_a.run([1])

assert test_a.run([1]) == 5074395

assert Computer(data.copy()).run([5, 1]) == 8346937, "Running with input 5 failed"
