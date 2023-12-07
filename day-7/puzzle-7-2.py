from functools import cmp_to_key

def compare(item1, item2):
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    if item1[3] > item2[3]:
        return -1
    elif item1[3] < item2[3]:
        return 1
    elif item1[3] == item2[3]:
        for i in range(5):
            if cards.index(item1[0][i]) < cards.index(item2[0][i]):
                return 1
            elif cards.index(item1[0][i]) > cards.index(item2[0][i]):
                return -1
        return 0


file = open('input.txt', 'r')
lines = file.readlines()

result = 0

all_results = []

for line in lines:
    line = line.split(' ')
    my_cards = line[0]
    bid = int(line[1])

    card_results = []

    for card in my_cards:
        index = next((i for i, item in enumerate(card_results) if item[0] == card), -1)
        if card != 'J':
            if index != -1:
                card_results[index][1] += 1
            else:
                card_results.append([card, 1])

    jokers_count = sum(card == 'J' for card in my_cards)
    if 0 < jokers_count < 5:
        max_value = max(result[1] for result in card_results)
        el = next((i for i, item in enumerate(card_results) if item[1] == max_value), -1)
        card_results[el][1] += jokers_count
    elif jokers_count == 5:
        card_results.append(['J', 5])

    if any(card[1] == 5 for card in card_results):
        range_number = 0
    elif any(card[1] == 4 for card in card_results):
        range_number = 1
    elif any(card[1] == 3 for card in card_results) and any(card[1] == 2 for card in card_results):
        range_number = 2
    elif any(card[1] == 3 for card in card_results) and sum(card[1] == 1 for card in card_results) == 2:
        range_number = 3
    elif sum(card[1] == 2 for card in card_results) == 2:
        range_number = 4
    elif sum(card[1] == 2 for card in card_results) == 1:
        range_number = 5
    else:
        range_number = 6

    all_results.append([my_cards, bid, card_results, range_number])

all_results = sorted(all_results, key=cmp_to_key(compare))

result = 0
for i, score in enumerate(all_results):
    result += (i + 1) * score[1]

print(result)