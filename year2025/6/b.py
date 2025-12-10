from linereader import read_file
import re
data = read_file('test.input.txt')
#data = read_file('input.txt')

def clean_line(line):
    cleaned_data = re.sub(r'\.{2,}', '.', line)
    return cleaned_data

results = []
for line_index in range(0, len(data)):
    cleaned = clean_line(data[line_index])
    print(cleaned)

    start = 0
    end = 0
    found_number_start = False
    found_number_end = False
    result = []

    for char_index in range(0, len(cleaned)):
        char = cleaned[char_index]
        if char.isnumeric():
            found_number_start = True
        if found_number_start and not char.isnumeric():
            end = char_index
            found_number_end = True

        
    results.append(cleaned[start:end])

print(results)
