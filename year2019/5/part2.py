from linereader import read_line

POSITION_MODE = 0
IMMEDIATE_MODE = 1


def value_from_mode(mode, instruction, program):
    return program[instruction] if mode == POSITION_MODE else instruction


def add(args):
    return args[0] + args[1]


def multiply(args):
    return args[0] * args[1]


def run(program, program_input):
    instruction_set = {
        1: add,
        2: multiply,
    }

    pc = 0
    while pc < len(program):
        mode_1 = program[pc] // 100 % 10
        mode_2 = program[pc] // 1000 % 10
        opcode = program[pc] % 100

        if opcode == 99:
            break

        p1 = program[pc + 1]
        p2 = program[pc + 2]
        store_address = program[pc + 3]

        if opcode == 1 or opcode == 2:
            operation = instruction_set[opcode]

            r1 = value_from_mode(mode_1, p1, program)
            r2 = value_from_mode(mode_2, p2, program)

            program[store_address] = operation([r1, r2])
            pc += 4

        elif opcode == 3:
            program[store_address] = program_input
            pc += 2

        elif opcode == 4:
            value = value_from_mode(mode_1, p1, program)
            pc += 2

            print(value)

        elif opcode == 5:
            # jump-if-true
            r1 = value_from_mode(mode_1, p1, program)
            r2 = value_from_mode(mode_2, p2, program)

            if r1 is not 0:
                pc = r2
            else:
                pc += 3

        elif opcode == 6:
            # jump-if-false
            r1 = value_from_mode(mode_1, p1, program)
            r2 = value_from_mode(mode_2, p2, program)

            if r1 is 0:
                pc = r2
            else:
                pc += 3

        elif opcode == 7:
            # less than
            r1 = value_from_mode(mode_1, p1, program)
            r2 = value_from_mode(mode_2, p2, program)

            if r1 < r2:
                program[store_address] = 1
            else:
                program[store_address] = 0

            pc += 4

        elif opcode == 8:
            r1 = value_from_mode(mode_1, p1, program)
            r2 = value_from_mode(mode_2, p2, program)

            if r1 == r2:
                program[store_address] = 1
            else:
                program[store_address] = 0

            pc += 4


data = [int(x) for x in read_line('5.input.txt', ',')]

run(data, 5)
