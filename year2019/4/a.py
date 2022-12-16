start = 146810
end = 612564

total = 0

for i in range(start, end + 1):
    string_number = str(i)

    double_digits = False
    increasing_order = True

    for j in range(1, len(string_number)):
        cur = int(string_number[j])
        prev = int(string_number[j - 1])

        if cur < prev:
            increasing_order = False

        elif cur == prev:
            if str(i).count(str(cur)) == 2:
                double_digits = True

    if double_digits and increasing_order:
        total += 1

print(total)
