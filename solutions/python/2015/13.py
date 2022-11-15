from typing import List
from itertools import permutations
import re


def neighbors(arrangement):
    for i in range(len(arrangement)):
        yield (
            arrangement[i],
            arrangement[i - 1],
            arrangement[(i + 1) % len(arrangement)],
        )


def run(inp: List[str]):
    shifts = [
        (a[0], int(a[2]) if a[1] == "gain" else -int(a[2]), a[3])
        for a in re.findall(
            r"(\w+) would (lose|gain) (\d+) happiness units? by sitting next to (\w+)",
            "\n".join(inp),
        )
    ]
    people = list(set(shift[0] for shift in shifts))
    mapped_shifts = {p: {a[2]: a[1] for a in shifts if a[0] == p} for p in people}

    def calc_happiness(arrangement: List[str]):
        happiness = 0
        for person, left, right in neighbors(arrangement):
            if person == "self":
                continue
            happiness += (mapped_shifts[person][left] if left != "self" else 0) + (
                mapped_shifts[person][right] if right != "self" else 0
            )
        return happiness

    print(max(calc_happiness(list(perm)) for perm in permutations(people)))

    print(max(calc_happiness(list(perm)) for perm in permutations(people + ["self"])))
