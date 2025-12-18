from common.solution import Solution
from common.parsing import extract_brackets, extract_parens, extract_braces
from itertools import combinations


class Day(Solution):
    def parse_input(self, raw: str):
        return [x for x in raw.strip().split("\n")]

    def read_line(self, line):
        """Parse a line into indicator, buttons, and joltage"""
        indicator = [int(c == "#") for c in extract_brackets(line)]
        buttons = [[int(x) for x in btn.split(",")] for btn in extract_parens(line)]
        joltage = [int(x) for x in extract_braces(line).split(",")]

        return indicator, buttons, joltage

    def create_matrix(self, indicator, buttons):
        """Create augmented matrix for GF(2) linear system"""
        n = len(indicator)
        m = len(buttons)

        matrix = [[0 for _ in range(m + 1)] for _ in range(n)]

        for y in range(n):
            for x in range(m):
                if y in buttons[x]:
                    matrix[y][x] = 1
            # Add goal as last column
            matrix[y][m] = indicator[y]

        return matrix

    def combine_rows(self, pivot, target):
        """XOR two rows in GF(2)"""
        row = []
        for i in range(len(pivot)):
            a = pivot[i]
            b = target[i]
            row.append(a ^ b)
        return row

    def swap_rows(self, matrix, from_row, to_row):
        """Swap two rows in matrix"""
        matrix[from_row], matrix[to_row] = matrix[to_row], matrix[from_row]

    def gf2_rref(self, matrix):
        """Gaussian elimination in GF(2) to get RREF"""
        n_rows = len(matrix)
        n_cols = len(matrix[0]) - 1
        pivot_info = []
        row = 0

        for col in range(n_cols):
            pivot_row = None
            for r in range(row, n_rows):
                if matrix[r][col] == 1:
                    pivot_row = r
                    break
            if pivot_row is None:
                continue

            if pivot_row != row:
                self.swap_rows(matrix, pivot_row, row)

            pivot_info.append((row, col))

            for r in range(row + 1, n_rows):
                if matrix[r][col] == 1:
                    matrix[r] = self.combine_rows(matrix[row], matrix[r])

            row += 1

        for pivot_row, pivot_col in reversed(pivot_info):
            for r in range(pivot_row):
                if matrix[r][pivot_col] == 1:
                    matrix[r] = self.combine_rows(matrix[pivot_row], matrix[r])

        return pivot_info

    def part1(self):
        """Solve using GF(2) linear algebra"""
        total = 0

        for i in range(len(self.data)):
            indicator, buttons, joltage = self.read_line(self.data[i])
            matrix = self.create_matrix(indicator, buttons)
            pivot_info = self.gf2_rref(matrix)

            n_cols = len(matrix[0]) - 1
            pivot_cols = set(col for _, col in pivot_info)
            free_cols = [col for col in range(n_cols) if col not in pivot_cols]

            min_presses = None

            for num_free_pressed in range(len(free_cols) + 1):
                for pressed_free_cols in combinations(free_cols, num_free_pressed):
                    solution = [0] * n_cols

                    for col in pressed_free_cols:
                        solution[col] = 1

                    for pivot_row, pivot_col in reversed(pivot_info):
                        val = matrix[pivot_row][-1]
                        for col in range(n_cols):
                            if col != pivot_col:
                                val ^= matrix[pivot_row][col] * solution[col]
                        solution[pivot_col] = val

                    presses = sum(solution)
                    if min_presses is None or presses < min_presses:
                        min_presses = presses

            total += min_presses

        return total

    def part2(self):
        try:
            from scipy.optimize import milp, LinearConstraint, Bounds
            import numpy as np
        except ImportError:
            return 0

        total = 0
        for i in range(len(self.data)):
            _, buttons, joltage = self.read_line(self.data[i])

            n_counters = len(joltage)
            n_buttons = len(buttons)

            A_eq = np.zeros((n_counters, n_buttons))
            for j, btn in enumerate(buttons):
                for counter_idx in btn:
                    if counter_idx < n_counters:
                        A_eq[counter_idx][j] = 1

            b_eq = np.array(joltage, dtype=float)

            c = np.ones(n_buttons)

            bounds = Bounds(lb=0, ub=np.inf)
            constraints = LinearConstraint(A_eq, b_eq, b_eq)

            integrality = np.ones(n_buttons)

            result = milp(
                c, constraints=constraints, bounds=bounds, integrality=integrality
            )

            if result.success:
                total += int(round(result.fun))
            else:
                return 0

        return total


Day().solve()
