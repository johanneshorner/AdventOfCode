from collections import defaultdict

STEPS = 40

with open("input.in") as file:
    template, _, *insertion_rules = file.read().splitlines()
    insertion_rules = dict(rule.split(" -> ") for rule in insertion_rules)

def apply_step(polymers: defaultdict, insertion_rules):
    for polymer, count in polymers.copy().items():
        polymers_new[polymer[0] + insertion_rules[polymer[0 : 2]]] += polymers[polymer]
        polymers_new[polymer] -= polymers[polymer]
    return polymers_new

polymers = defaultdict(int, {template[i : i + 3] : 1 for i in range(len(template) - 2)})

for _ in range(STEPS):
    polymers = apply_step(polymers, insertion_rules)