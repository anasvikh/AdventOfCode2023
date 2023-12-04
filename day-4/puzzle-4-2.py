file = open('input.txt', 'r')
lines = file.readlines()

cards_count = [1] * len(lines)

for i, line in enumerate(lines):
    numbers = line.split(': ')[1].split(' | ')
    win_numbers = list(filter(lambda number: number, numbers[0].strip().split(' ')))
    my_numbers = list(filter(lambda number: number, numbers[1].strip().replace('\n', '').split(' ')))
    my_win_numbers_count = sum(number in win_numbers for number in my_numbers)

    for x in range(my_win_numbers_count):
        cards_count[i+x+1] += 1 * cards_count[i]

result = sum(cards_count)
print(result)