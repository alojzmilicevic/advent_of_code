from linereader import read_file

data = read_file('input.txt')

def max_subsequence(digits, n):
    digits = list(map(int, digits))
    length = len(digits)
    result: list[int] = []
    start = 0

    for i in range(n):
        max_index = length - (n - len(result))

        best_digit = -1
        best_pos = start
        for pos in range(start, max_index + 1):
            if digits[pos] > best_digit:
                best_digit = digits[pos]
                best_pos = pos
            if best_digit == 9:
                break

        result.append(str(best_digit))
        start = best_pos + 1

    return "".join(result)


count = 0
for line in data:
    count += int(max_subsequence(line, 12))

print(count)


