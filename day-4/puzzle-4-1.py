file = open('input.txt', 'r')
lines = file.readlines()

result = 0

for line in lines:
    numbers = line.split(': ')[1].split(' | ')
    win_numbers = list(filter(lambda number: number, numbers[0].strip().split(' ')))
    my_numbers = list(filter(lambda number: number, numbers[1].strip().replace('\n', '').split(' ')))
    my_win_numbers_count = sum(number in win_numbers for number in my_numbers)
    result += 2**(my_win_numbers_count-1) if my_win_numbers_count > 0 else 0
    
print(result)