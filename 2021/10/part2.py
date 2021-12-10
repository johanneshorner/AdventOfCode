with open("input.in") as file:
    lines = [[chunk_part for chunk_part in line.strip()] for line in file]

opening_lookup = {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}
closing_lookup = {")" : "(", "]" : "[", "}" : "{", ">" : "<"}

complete_lookup = {")" : 1, "]" : 2, "}" : 3, ">" : 4}

def is_corrupt(line: list[str]) -> bool:
    opening_stack = []
    for chunk_part in line:
        if chunk_part in opening_lookup:
            opening_stack.append(chunk_part)
        else:
            if len(opening_stack) != 0:
                if opening_lookup[opening_stack.pop()] == chunk_part:
                    continue
            return True
    return False

lines = [line for line in lines if not is_corrupt(line)]

sub_sums = [0] * len(lines)

for idx in range(len(lines)):
    opening_stack = []
    for chunk_part in lines[idx]:
        if chunk_part in opening_lookup:
            opening_stack.append(chunk_part)
        else:
            if len(opening_stack) != 0:
                if opening_lookup[opening_stack.pop()] == chunk_part:
                    continue
    for _ in range(len(opening_stack)):
        sub_sums[idx] = sub_sums[idx] * 5 + complete_lookup[opening_lookup[opening_stack.pop()]]

sub_sums.sort()
print(sub_sums[int(len(sub_sums)/2)])


            