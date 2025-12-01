import sys
sys.path.insert(0, '../../')
from linereader import read_line

data = [x for x in read_line('input.txt', ",")]

count = 0
for r in data:
    parts = r.split("-")
    first = int(parts[0])
    second = int(parts[1])

    for i in range(first, second + 1):
        s = str(i)

        for j in range(1, len(s)):
            chunks = len(s) // j
            if chunks > 0 and len(s) % j == 0:
                all_equal = True
                first_chunk = s[0:j]
                for k in range(1, chunks):
                    if s[k*j:(k+1)*j] != first_chunk:
                        all_equal = False
                        break
                if all_equal:
                    count += int(s)
                    break

print(count)

