def get_digits_near_star(x, y) -> list:
    left_x = x - 1 if x - 1 > 0 else 0
    right_x = x + 1 if x + 1 < len(lines[0]) - 1 else len(lines[0]) - 1
    top_y = y - 1 if y - 1 > 0 else 0
    bottom_y = y + 1 if y + 1 < len(lines) - 1 else len(lines) - 1

    result = []

    if lines[top_y][left_x].isdigit():
        result.append((left_x, top_y, lines[top_y][left_x]))
    if lines[top_y][x].isdigit():
        result.append((x, top_y, lines[top_y][x]))
    if lines[top_y][right_x].isdigit():
        result.append((right_x, top_y, lines[top_y][right_x]))
    if lines[y][left_x].isdigit():
        result.append((left_x, y, lines[y][left_x]))
    if lines[y][right_x].isdigit():
        result.append((right_x, y, lines[y][right_x]))
    if lines[bottom_y][left_x].isdigit():
        result.append((left_x, bottom_y, lines[bottom_y][left_x]))
    if lines[bottom_y][x].isdigit():
        result.append((x, bottom_y, lines[bottom_y][x]))
    if lines[bottom_y][right_x].isdigit():
        result.append((right_x, bottom_y, lines[bottom_y][right_x]))
    return result


file = open('input.txt', 'r')
lines = file.readlines()

result = 0

numbers_coords = [[]]

for y, line in enumerate(lines):
    for x, symbol in enumerate(line):
        current_number_coords = numbers_coords[-1]
        if symbol.isdigit():
            current_number_coords.append((x, y, symbol))
        elif current_number_coords:
            numbers_coords.append([])

stars_coords = []

for y, line in enumerate(lines):
    for x, symbol in enumerate(line):
        if symbol == '*':
            digits = get_digits_near_star(x, y)
            star_numbers_coords = []
            for digit in digits:
                for coords in numbers_coords:
                    if digit in coords and coords not in star_numbers_coords:
                        star_numbers_coords.append(coords)
                        break
            if len(star_numbers_coords) == 2:
                numbers = []
                for coords in star_numbers_coords:
                    number_str = ''
                    for coord in coords:
                        number_str += coord[2]
                    numbers.append(int(number_str))
                print(numbers )
                result += numbers[0] * numbers[1]

print(result)