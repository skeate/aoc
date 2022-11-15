from typing import List


def match(i, inp):
    preamble = set(inp[i - 25 : i])
    found = False
    for j in range(25):
        if (inp[i] - inp[i - j]) in preamble:
            found = True
    if not found:
        return inp[i]
    return None


def run(inp: List[str]):
    inp = [*map(int, inp)]
    for i in range(25, len(inp)):
        p1 = match(i, inp)
        if p1 is not None:
            print(p1)
            break

    for i in range(len(inp)):
        j = i + 1
        conts = [inp[i], inp[j]]
        while sum(conts) < p1:
            j += 1
            conts.append(inp[j])
        if sum(conts) == p1:
            print(min(conts) + max(conts))
            break
