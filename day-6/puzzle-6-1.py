file = open('input.txt', 'r')
lines = file.readlines()

result = 1

raw_times = lines[0].split(': ')[1].replace('\n', '').split(' ')
times = list(int(i) for i in filter(lambda number: number, raw_times))

raw_distances = lines[1].split(': ')[1].replace('\n', '').split(' ')
distances = list(int(i) for i in filter(lambda number: number, raw_distances))

for i, time in enumerate(times):
    count = 0
    for j in range(time):
        speed = j
        distance = time - j
        moving_time = time - j
        distance = speed * moving_time

        print(speed, distance)
        if distance > distances[i]:
            count += 1
    result *= count

print(result)


