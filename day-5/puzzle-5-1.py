def count(
        lines,
        line_for_search: str,
        items
):
    index = lines.index(line_for_search)
    map_list = []
    iterable = 1
    while True:
        if index + iterable >= len(lines):
            break

        line_for_search = lines[index + iterable]
        if line_for_search == '\n':
            break
        map_list.append(line_for_search.replace('\n', '').split(' '))
        map_list.sort(key=lambda x: x[1])
        iterable += 1

    map_list.sort(key=lambda x: int(x[1]))
    result_items = []
    for item in items:
        current_seed_to_fertilizer = list(filter(lambda ir: int(ir[1]) <= int(item), map_list))
        if current_seed_to_fertilizer and int(item) <= int(current_seed_to_fertilizer[-1][1]) + int(
                current_seed_to_fertilizer[-1][2]):
            result_item = int(item) + (int(current_seed_to_fertilizer[-1][0]) - int(current_seed_to_fertilizer[-1][1]))
        else:
            result_item = int(item)
        result_items.append(result_item)
    return result_items

file = open('input.txt', 'r')
lines = file.readlines()

result = 0

seeds = lines[0].split(': ')[1].strip().replace('\n', '').split(' ')

text_lines = []

for i, line in enumerate(lines):
    if i != 0 and line != '\n' and not line[0].isdigit():
        text_lines.append(line)

results = seeds
for line in text_lines:
    results = count(
        lines,
        line,
        results
    )
print(min(results))
