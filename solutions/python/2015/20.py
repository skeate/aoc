from typing import List
import math


def run(inp: List[str]):
    inp = 33100000

    houses = [0] * (inp // 10)
    for i in range(1, len(houses)):
        for j in range(i, len(houses), i):
            houses[j] += i * 10
    for i in range(len(houses)):
        if houses[i] >= inp:
            print(i)
            break

    houses = [0] * (inp // 10)
    for i in range(1, len(houses)):
        for j in range(1, 50):
            if (i * j) < len(houses):
                houses[j * i] += i * 11
    for i in range(len(houses)):
        if houses[i] >= inp:
            print(i)
            break
