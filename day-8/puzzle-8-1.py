import re

file = open('input.txt', 'r')
lines = file.readlines()

result = 0

pattern = lines[0].replace('\n', '')

items = []
for i in range (2, len(lines)):
    line = lines[i]
    current = re.search('(.+?) =', line).group(1)
    left = re.search(r'\((.+?),', line).group(1)
    right = re.search(r', (.+?)\)', line).group(1)
    items.append((current, left, right))

current_element = next(x for x in items if x[0] == 'AAA')
while True:
    pattern_index = result % len(pattern)
    current_element_name = current_element[1] if pattern[pattern_index] == 'L' else current_element[2]
    current_element = next(x for x in items if x[0] == current_element_name)
    result += 1
    if current_element[0] == 'ZZZ':
        break
print(result)