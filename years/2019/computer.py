from util import *


class Computer:
    def __init__(self, program, argv=None):
        if argv is None:
            argv = []
        self.program = program
        self.output_buffer = []
        self.input_buffer = argv
        self.pc = 0
        self.halted = False

    def output(self, elem):
        self.output_buffer.append(elem)

    def input(self, in_data):
        for data in in_data:
            self.input_buffer.append(data)

    def decode(self, parameter):
        mode = parameter.mode
        pos = self.program[parameter.offset]

        if mode == Mode.POSITION_MODE:
            return self.program[pos]

        elif mode == Mode.IMMEDIATE_MODE:
            return pos

        elif mode == Mode.RELATIVE_MODE:
            pass

    def run(self, in_data, debug=False):
        store_address = -1
        interrupted = False

        self.input(in_data)

        while not self.halted:
            affected_registers = []

            P1 = Parameter(self.program[self.pc] // 100 % 10, self.pc + 1)
            P2 = Parameter(self.program[self.pc] // 1000 % 10, self.pc + 2)
            opcode = self.program[self.pc] % 100

            if opcode == 99:
                self.halted = True
                if len(self.output_buffer) > 0:
                    return self.output_buffer[-1]
                else:
                    return self.program[0]

            if interrupted:
                if debug:
                    print("Pc when halted: ", self.pc)
                return self.output_buffer[-1]

            P1 = self.decode(P1)

            if opcode != 3 and opcode != 4:
                P2 = self.decode(P2)
                store_address = self.program[self.pc + 3]

            # All available instructions follow
            if opcode == OP.ADD:
                self.program[store_address] = P1 + P2
                self.pc += 4

                if debug:
                    print("Adding", str(P1), "with", str(P2), "and storing the result in", str(store_address))
                    affected_registers.append(P1)
                    affected_registers.append(P2)
                    affected_registers.append(store_address)

            elif opcode == OP.MLT:
                self.program[store_address] = P1 * P2
                self.pc += 4

                if debug:
                    affected_registers.append(P1)
                    affected_registers.append(P2)
                    affected_registers.append(store_address)

            elif opcode == OP.GET:
                x = self.input_buffer.pop(0)
                reg = self.program[self.pc + 1]

                self.program[reg] = x

                if debug:
                    print("Inserting", str(x), "into", reg)
                    affected_registers.append(reg)

                self.pc += 2

            elif opcode == OP.PUT:
                self.output(P1)
                self.pc += 2
                interrupted = True

            elif opcode == OP.JUMP_IF_TRUE:
                if P1 is not 0:
                    self.pc = P2
                else:
                    self.pc += 3

            elif opcode == OP.JUMP_IF_FALSE:
                if P1 is 0:
                    self.pc = P2
                else:
                    self.pc = self.pc + 3

            elif opcode == OP.LESS_THAN:
                if P1 < P2:
                    self.program[store_address] = 1
                else:
                    self.program[store_address] = 0
                self.pc += 4

                if debug:
                    affected_registers.append(P1)
                    affected_registers.append(P2)
                    affected_registers.append(store_address)

            elif opcode == OP.EQUAL:
                if P1 == P2:
                    self.program[store_address] = 1
                else:
                    self.program[store_address] = 0
                self.pc += 4

                if debug:
                    affected_registers.append(P1)
                    affected_registers.append(P2)
                    affected_registers.append(store_address)

            if debug and opcode != OP.PUT:
                print("[", end="")
                for i in range(0, len(self.program)):
                    if i == self.pc:
                        print("-->[", end="")

                    if i in affected_registers:
                        print("**{", end="")

                    print(str(self.program[i]), end="")

                    if i in affected_registers:
                        print("}**", end="")

                    if i == self.pc:
                        print("]<--", end="")

                    if i is not len(self.program) - 1:
                        print(", ", end="")

                print("]", end="")
                input()
