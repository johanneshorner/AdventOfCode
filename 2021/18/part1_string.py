import functools

with open("input.in") as file:
    sf_numbers = [line.strip() for line in file]

def explode_numbers(number: str, idx, left, right):
    for i in range(idx - 1, 0, -1):
        if number[i].isnumeric():
            new_value = int(number[i]) + left
            number = number[:i] + str(new_value) + number[i + 1:]
            if new_value > 9: idx += 1 # two digit values increase string length
            break
    for i in range(idx + 1, len(number)):
        if number[i].isnumeric():
            number = number[:i] + str(int(number[i]) + right) + number[i + 1:]
            break
    return number

def reduce(number: str):
    #explode
    while True:
        number_old = number
        nest_count = 0
        for i in range(len(number) - 2):
            if number[i] == "[": nest_count += 1
            if number[i] == "]": nest_count -= 1
            if nest_count >= 5:
                if number[i].isnumeric() and number[i + 2].isnumeric():
                    left = int(number[i])
                    right = int(number[i + 2])
                    number = number[:i - 1] + "0" + number[i + 4:]
                    number = explode_numbers(number, i - 1, left, right)
                    break

        if number_old == number:
            #split
            for i in range(len(number) - 1):
                if number[i:i + 2].isnumeric():
                    value = int(number[i:i + 2])
                    left = int(value / 2) #rounded down
                    right = value - left #rounded up

                    number = number[:i] + "[" + str(left) + "," + str(right) + "]" + number[i + 2:]
                    break

        if number_old == number:
            break

    return number

def add(left, right) -> list:
    new_number = "[" + left + "," + right + "]"
    
    new_number = reduce(new_number)

    return new_number

result = functools.reduce(lambda a, b: add(a, b), sf_numbers)

def calc_magnitude(sf_number):
    left = 0
    right = 0

    if isinstance(sf_number[0], int):
        left += 3 * sf_number[0]
    else:
        left += 3 * calc_magnitude(sf_number[0])

    if isinstance(sf_number[1], int):
        right += 2 * sf_number[1]
    else:
        right += 2 * calc_magnitude(sf_number[1])

    return left + right

print(calc_magnitude(eval(result)))