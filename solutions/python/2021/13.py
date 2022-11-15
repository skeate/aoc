from typing import List

def print_dots(dots):
    xmax = max(dx for dx, dy in dots)
    ymax = max(dy for dx, dy in dots)
    for y in range(ymax + 1):
        for x in range(xmax + 1):
            print('#' if (x, y) in dots else ' ', end='')
        print('')

def run(inp: List[str]):
    dots = set([tuple(int(d) for d in i.strip().split(',')) for i in inp if ',' in i])
    folds = [tuple(d for d in i.strip()[11:] .split('=')) for i in inp if '=' in i]

    # print_dots(dots)

    for axis, num in folds:
        num = int(num)
        if axis == 'y':
            dots = set([(dx, num + num - dy if dy > num else dy) for dx, dy in dots])
        if axis == 'x':
            dots = set([(num + num - dx if dx > num else dx, dy) for dx, dy in dots])
        print(len(dots))
        # print_dots(dots)
