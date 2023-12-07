file = open('input.txt', 'r')
lines = file.readlines()

result = 0

time = int(lines[0].replace(' ', '').split(':')[1].replace('\n', ''))
win_distance = int(lines[1].replace(' ', '').split(':')[1].replace('\n', ''))

for j in range(time):
    speed = j
    distance = time - j
    moving_time = time - j
    distance = speed * moving_time
    print(speed, distance)
    if distance > win_distance:
        result += 1

print(result)


