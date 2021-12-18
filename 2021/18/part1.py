import functools

with open("input.in") as file:
    sf_numbers = [eval(line) for line in file]

def reduce(number, recursion_counter):
    if recursion_counter + 1 == 4:
        #explode
        pass

    


def add(left: list, right: list) -> list:
    new_number = []
    new_number.append(left)
    new_number.append(right)

    while reduce(new_number, 0):
        pass

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

print(calc_magnitude(result))