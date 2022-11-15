from typing import List

def neighbors(p):
    x, y = p
    return [
        (x + dx, y + dy)
        for dx in [-1, 0, 1]
        for dy in [-1, 0, 1]
        if (dy != 0 or dx != 0)
        and 0 <= y + dy < 10
        and 0 <= x + dx < 10
    ]

def run(inp: List[str]):
    energy_levels = [[int(c) for c in list(s.strip())] for s in inp]

    flashes = 0
    for _ in range(100):
        energy_levels = [[e + 1 for e in r] for r in energy_levels]
        flashed = set()
        check_flashes = True
        while check_flashes:
            check_flashes = False
            for y in range(len(energy_levels)):
                for x in range(len(energy_levels[y])):
                    if energy_levels[y][x] > 9 and (x,y) not in flashed:
                        flashed.add((x,y))
                        check_flashes = True
                        for nx, ny in neighbors((x,y)):
                            energy_levels[ny][nx] += 1

        flashes += len(flashed)
        for y in range(len(energy_levels)):
            for x in range(len(energy_levels[y])):
                if energy_levels[y][x] > 9:
                    energy_levels[y][x] = 0
        # for r in energy_levels:
        #     print(''.join(str(c) for c in r))
        # print()
    print(flashes)
    step = 100
    flashed = set()
    while len(flashed) != 100:
        step += 1
        energy_levels = [[e + 1 for e in r] for r in energy_levels]
        flashed = set()
        check_flashes = True
        while check_flashes:
            check_flashes = False
            for y in range(len(energy_levels)):
                for x in range(len(energy_levels[y])):
                    if energy_levels[y][x] > 9 and (x,y) not in flashed:
                        flashed.add((x,y))
                        check_flashes = True
                        for nx, ny in neighbors((x,y)):
                            energy_levels[ny][nx] += 1
        for y in range(len(energy_levels)):
            for x in range(len(energy_levels[y])):
                if energy_levels[y][x] > 9:
                    energy_levels[y][x] = 0
    print(step)
