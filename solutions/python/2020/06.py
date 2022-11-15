from typing import List

def run(inp: List[str]):
    xs = []
    x = []
    for line in inp:
        if line.strip() == "":
            xs.append(x)
            x = []
        else:
            x.append(set(line.strip()))
    xs.append(x)

    print(sum(len(set.union(*a)) for a in xs))
    print(sum(len(set.intersection(*a)) for a in xs))
