class Mode:
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1
    RELATIVE_MODE = 2


class OP:
    ADD = 1
    MLT = 2
    GET = 3
    PUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUAL = 8


class Parameter:
    def __init__(self, mode, offset):
        self.mode = mode
        self.offset = offset

