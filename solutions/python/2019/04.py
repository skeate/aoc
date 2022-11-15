from typing import List

def run(inp: List[str]):
    low, high = map(int, inp[0].strip().split('-'))

    count= 0
    for i in range(low,high + 1):
        if two_same(i) and ascending(i):
            count += 1

    print(count)

    count= 0
    for i in range(low,high + 1):
        if two_same_stricter(i) and ascending(i):
            count += 1

    print(count)

def two_same(n):
    return len(set(str(n))) < 6

def ascending(n):
    s= str(n)
    s1 = s[:-1]
    s2 = s[1:]
    for i,j in zip(s1,s2):
        if int(i) > int(j):
            return False
    return True


def two_same_stricter(n):
    cs = str(n)
    counts = {}
    for i in range(10):
        counts[i] = cs.count(str(i))
    return 2 in counts.values()

