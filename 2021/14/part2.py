from collections import defaultdict

def parse_input(input_str: str):
    template = input_str.split("\n\n")[0]
    insertion_rule_lines = input_str.split("\n\n")[1].split("\n")

    return (
        template,
        {left : right for left, right in (insertion_rule.split(" -> ") for insertion_rule in insertion_rule_lines)}
    )

with open("input.in") as file:
    template, insertion_rules = parse_input(file.read())

def apply_step(polymers, insertion_rules):
    polymers_new = polymers.copy()
    for polymer in polymers:
        polymers_new[polymer[0] + insertion_rules[polymer[0 : 2]]] += polymers[polymer]
        polymers_new[polymer] -= polymers[polymer]
    
    return polymers_new

polymers = defaultdict(int, {template[i : i + 3] : 1 for i in range(len(template) - 2)})
for i in range(1):
    polymers = apply_step(polymers, insertion_rules)

occurences = {char: 0 for char in set([char for polymer in polymers for char in polymer])}

for char in occurences:
    for polymer in polymers:
        if char in polymer:
            if char == template[0] or char == template[-1]:
                occurences[char] += (polymer.count(char) / 2) + 1
            else:
                occurences[char] += polymer.count(char) / 2

print(max(occurences.values()) - min(occurences.values()))