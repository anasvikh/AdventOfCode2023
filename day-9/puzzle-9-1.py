file = open('input.txt', 'r')
lines = file.readlines()

result = 0

for line in lines:
    history = [int(item) for item in line.replace('\n', '').split(' ')]
    current_history = history
    next_number = history[-1]
    while True:
        new_history = []
        for i, item in enumerate(current_history):
            if i+1 < len(current_history):
                new_history.append(current_history[i+1]-current_history[i])
        if sum(card == 0 for card in new_history) == len(new_history):
            break
        else:
            next_number += new_history[-1]
            current_history = new_history
    result += next_number
print(result)