from itertools import permutations, cycle
from linereader import read_line
from intcode_computer.computer import Computer

data = [int(x) for x in read_line('7.input.txt', ',')]

# Part 1

ans = 0
phase_set = permutations(range(5), 5)

for phase_settings in phase_set:
    output = 0

    for phase in phase_settings:
        output = Computer(data.copy()).run([phase, output])

    ans = max(ans, output)

print("Ans 1:", ans)
expected_result = 34686
assert ans == expected_result, "ERROR: ans was (" + str(ans) + ") should have been (" + str(expected_result) + ")"

# Part 2
ans = 0
phase_set = list(permutations(range(5, 10), 5))

for phase in phase_set:
    amplifiers = [Computer(data.copy(), [phase[i]]) for i in range(0, 5)]
    amp_iter = cycle(amplifiers)

    output = 0
    while not amplifiers[4].halted:
        output = next(amp_iter).run([output])

    ans = max(ans, output)

print("Ans 2:", ans)
expected_result = 36384144
assert ans == expected_result, "ERROR: ans was (" + str(ans) + ") should have been (" + str(expected_result) + ")"
