input = open("input.in", "r").read()

crab_horizontal_positions = [int(pos) for pos in input.split(',')]

fuel_usages = []

for pos in range(0, max(crab_horizontal_positions), 1):
    fuel_usages.append(0)
    print(pos)
    for crab_pos in crab_horizontal_positions:
        fuel_usages[pos] += sum(range(1, abs(crab_pos - pos) + 1, 1))

print(min(fuel_usages))