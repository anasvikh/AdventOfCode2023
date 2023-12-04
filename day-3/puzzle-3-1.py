def is_good_number(x, y) -> bool:
    left_x = x-1 if x-1 > 0 else 0
    right_x = x+1 if x+1 < len(lines[0])-1 else len(lines[0])-1
    top_y = y-1 if y-1 > 0 else 0
    bottom_y = y+1 if y+1 < len(lines)-1 else len(lines)-1
        
    return (
        lines[top_y][left_x] in symbols or
        lines[top_y][x] in symbols or
        lines[top_y][right_x] in symbols or
        lines[y][left_x] in symbols or
        lines[y][right_x] in symbols or
        lines[bottom_y][left_x] in symbols or
        lines[bottom_y][x] in symbols or
        lines[bottom_y][right_x] in symbols
    )


file = open('input.txt', 'r')
lines = file.readlines()

result = 0

symbols = ['*', '+', '$', '#', '-', '%', '@', '=', '&', '/']

for y, line in enumerate(lines):
    current_number_coords = []
    for x, symbol in enumerate(line):
        if symbol.isdigit():
            current_number_coords.append((x, y, symbol))
        elif current_number_coords:
            good_numbers = [coord for coord in current_number_coords if is_good_number(coord[0], coord[1])]
            if good_numbers:
                number_str = ''
                for coord in current_number_coords:
                    number_str += coord[2]
                result += int(number_str)
            current_number_coords = []
print(result)