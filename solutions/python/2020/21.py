from typing import List
from copy import deepcopy

def simplify(d):
    changed = True
    while changed:
        changed = False
        for key in sorted(d.keys(), key=lambda k: len(d[k])):
            if len(d[key]) == 1:
                for k, v in d.items():
                    if k != key and len(v & d[key]) > 0:
                        d[k] -= d[key]
                        changed = True
    return d

def run(inp: List[str]):
    ingredients = [set(l.split(' (')[0].split(' ')) for l in inp]
    allergens = [set(l.split('(contains ')[1].strip(')\n').split(', ')) for l in inp]

    all_allergens = set.union(*allergens)


    possible_allergens = set()
    for allergen in all_allergens:
        possible_allergens |= set.intersection(*[i for a, i in zip(allergens, ingredients) if allergen in a])
    impossible_allergens = [i - possible_allergens for i in ingredients]
    print(sum(len(ia) for ia in impossible_allergens))

    possible_matches = {}
    for allergen in all_allergens:
        possible_matches[allergen] = set.intersection(*[i & possible_allergens for a, i in zip(allergens, ingredients) if allergen in a])
    simplify(possible_matches)
    print(','.join(list(i)[0] for a, i in sorted(possible_matches.items(), key=lambda a: a[0])))
