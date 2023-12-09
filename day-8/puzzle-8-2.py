import re
import math

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

start_items_array = list(filter(lambda i: i[0][2] == 'A', items))

count = 0
zz = [None] * 6

while True:
    pattern_index = count % len(pattern)
    count += 1
    for i, item in enumerate(start_items_array):
        current_element_name = item[1] if pattern[pattern_index] == 'L' else item[2]
        current_element = next(x for x in items if x[0] == current_element_name)
        start_items_array[i] = current_element
        if current_element[0][2] == 'Z' and zz[i] == None:
            zz[i] = count
    if not any(not item for item in zz):
        result = math.lcm(*zz)
        break

print(result)