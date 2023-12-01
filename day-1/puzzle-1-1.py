file = open('input.txt', 'r')
lines = file.readlines()

result = 0

for line in lines:
    for symbol in line:
        if symbol.isdigit():
            result += int(symbol)*10
            break

    line = line[::-1]

    for symbol in line:
        if symbol.isdigit():
            result += int(symbol)
            break
        
print(result)