from typing import List


def solve(numbers, upper):
    n = numbers[-1]
    lasts = upper * [0]
    for i, num in enumerate(numbers[:-1]):
        lasts[num] = i + 1
    for x in range(len(numbers), upper):
        y = 0 if lasts[n] == 0 else (x - lasts[n])
        lasts[n], n = x, y
    print(n)


def run(inp: List[str]):
    numbers = [*map(int, inp[0].split(','))]
    solve(numbers, 2020)
    solve(numbers, 30_000_000)
