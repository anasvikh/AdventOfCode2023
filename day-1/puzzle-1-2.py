file = open('input.txt', 'r')
lines = file.readlines()

result = 0

for line in lines:
    line = (line
        .replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "f4r")
        .replace("five", "f5e")
        .replace("six", "s6x")
        .replace("seven", "s7n")
        .replace("eight", "e8t")
        .replace("nine", "n9e")
    )

    for symbol in line:
        if symbol.isdigit():
            result += int(symbol) * 10
            break

    line = line[::-1]

    for symbol in line:
        if symbol.isdigit():
            result += int(symbol)
            break

print(result)