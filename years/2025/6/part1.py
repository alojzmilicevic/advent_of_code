from common.solution import Solution
import sys


class Day(Solution):
    def parse_input(self, raw: str):
        lines = raw.strip().split("\n")
        return lines

    def part1(self):
        lines = self.data

        if not lines:
            return 0

        max_len = max(len(line) for line in lines)
        padded = [line.ljust(max_len) for line in lines]

        columns_data = []
        for col_idx in range(max_len):
            column_chars = [padded[row_idx][col_idx] for row_idx in range(len(padded))]
            columns_data.append(column_chars)

        problems = []
        current_problem = []

        for col_idx, col_chars in enumerate(columns_data):
            if all(c == " " for c in col_chars):
                if current_problem:
                    problems.append(current_problem)
                    current_problem = []
            else:
                current_problem.append(col_chars)

        if current_problem:
            problems.append(current_problem)

        grand_total = 0

        for problem_cols in problems:
            num_rows = len(problem_cols[0])
            numbers = []
            operation = None

            for row_idx in range(num_rows):
                row_str = "".join(col[row_idx] for col in problem_cols).strip()

                if row_idx == num_rows - 1:
                    if "+" in row_str:
                        operation = "+"
                    elif "*" in row_str:
                        operation = "*"
                else:
                    if row_str:
                        try:
                            numbers.append(int(row_str))
                        except ValueError:
                            pass

            if operation and numbers:
                if operation == "+":
                    result = sum(numbers)
                elif operation == "*":
                    result = 1
                    for num in numbers:
                        result *= num
                else:
                    continue

                grand_total += result

        return grand_total

    def part2(self):
        lines = self.data

        if not lines:
            return 0

        max_len = max(len(line) for line in lines)
        padded = [line.ljust(max_len) for line in lines]

        columns_data = []
        for col_idx in range(max_len):
            column_chars = [padded[row_idx][col_idx] for row_idx in range(len(padded))]
            columns_data.append(column_chars)

        problems = []
        current_problem = []

        for col_idx, col_chars in enumerate(columns_data):
            if all(c == " " for c in col_chars):
                if current_problem:
                    problems.append(current_problem)
                    current_problem = []
            else:
                current_problem.append(col_chars)

        if current_problem:
            problems.append(current_problem)

        grand_total = 0

        for problem_cols in problems:
            num_rows = len(problem_cols[0])
            numbers = []
            operation = None

            for col_idx in reversed(range(len(problem_cols))):
                col_chars = problem_cols[col_idx]

                digits = ""
                for row_idx in range(num_rows):
                    char = col_chars[row_idx]
                    if char.isdigit():
                        digits += char
                    elif char == "+":
                        operation = "+"
                    elif char == "*":
                        operation = "*"

                if digits:
                    numbers.append(int(digits))

            if operation and numbers:
                if operation == "+":
                    result = sum(numbers)
                elif operation == "*":
                    result = 1
                    for num in numbers:
                        result *= num
                else:
                    continue

                grand_total += result

        return grand_total


Day(test="test" in sys.argv).solve()
