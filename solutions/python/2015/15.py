from functools import reduce
from typing import List
import re

def prod(l):
    return reduce(lambda a,b: a * b, l)

def minz(n):
    return n if n >= 0 else 0

def run(inp: List[str]):
    ingredients = {
        i: [int(x) for x in [c, d, f, t, cc]]
        for i, c, d, f, t, cc in (
            re.findall(
                r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)",
                s.strip(),
            )[0]
            for s in inp
        )
    }
    max_score = 0
    for f in range(0, 101):
        for c in range(0, 101 - f):
            for b in range(0, 101 - f - c):
                s = 100 - f - c - b
                score = prod([
                    minz(ingredients["Frosting"][i] * f
                    + ingredients["Candy"][i] * c
                    + ingredients["Butterscotch"][i] * b
                    + ingredients["Sugar"][i] * s)
                    for i in range(4)
                ])
                if score > max_score:
                    max_score = score
    print(max_score)

    max_score = 0
    for f in range(0, 101):
        for c in range(0, 101 - f):
            for b in range(0, 101 - f - c):
                s = 100 - f - c - b
                calories = ingredients["Frosting"][4] * f + ingredients["Candy"][4] * c + ingredients["Butterscotch"][4] * b + ingredients["Sugar"][4] * s
                if calories != 500:
                    continue
                score = prod([
                    minz(ingredients["Frosting"][i] * f
                    + ingredients["Candy"][i] * c
                    + ingredients["Butterscotch"][i] * b
                    + ingredients["Sugar"][i] * s)
                    for i in range(4)
                ])
                if score > max_score:
                    max_score = score
    print(max_score)
