import re

file = open('input.txt', 'r')
lines = file.readlines()

result = 0

for line in lines:
    game_id = int(re.search('Game (.+?):', line).group(1))
    print(game_id)
    
    red_count = []
    green_count = []
    blue_count = []
    
    rounds = line.split(': ')[1].split('; ')
    
    for round in rounds:
        colors = round.split(', ')
        
        for color_str in colors:
            count = int(re.search('(.+?) ', color_str).group(1))
            color = re.search(' (.+?)$', color_str).group(1)
            
            if color == 'red':
                red_count.append(count)
            elif color == 'green':
                green_count.append(count)
            else:
                blue_count.append(count)
                
    round_count = max(red_count) * max(green_count) * max(blue_count)
    result += round_count
    
print(result)