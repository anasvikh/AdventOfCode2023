import re

file = open('input.txt', 'r')
lines = file.readlines()

max_red_count = 12
max_green_count = 13
max_blue_count = 14

result = 0

for line in lines:
    game_id = int(re.search('Game (.+?):', line).group(1))
    print(game_id)
    
    rounds = line.split(': ')[1].split('; ')
    
    for round in rounds:
        colors = round.split(', ')
        
        for color_str in colors:
            count = int(re.search('(.+?) ', color_str).group(1))
            color = re.search(' (.+?)$', color_str).group(1)
            
            if (
                (color == 'red' and count > max_red_count)
                or (color == 'green' and count > max_green_count)
                or (color == 'blue' and count > max_blue_count)
                ):
                    break
        else:
            continue
        break
    else:
        result += game_id
        continue
    
print(result)
                    