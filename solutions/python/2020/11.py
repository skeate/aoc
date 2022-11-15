from typing import List
from copy import deepcopy
from functools import cache
import itertools

def step(seats: List[List[str]]):
    new_seats = deepcopy(seats)
    for r in range(1, len(seats) - 1):
        for c in range(1, len(seats[r]) - 1):
            neighbors = [seats[y][x] for x,y in itertools.product(range(c-1, c+2), range(r-1, r+2)) if not (x == c and y == r)]
            occupied_neighbors = neighbors.count('#')
            if seats[r][c] == 'L' and occupied_neighbors == 0:
                new_seats[r][c] = '#'
            elif seats[r][c] == '#' and occupied_neighbors >= 4:
                new_seats[r][c] = 'L'
    return new_seats

def eq(a: List[List[str]], b: List[List[str]]):
    for r in range(1, len(a) - 1):
        for c in range(1, len(a[r]) - 1):
            if a[r][c] != b[r][c]:
                return False
    return True

def pp(s: List[List[str]]):
    print('-' * len(s[0]))
    for r in s:
        print(''.join(r))

lookup = {}
def find_neighbors(seats, r: int, c: int, dr: int, dc: int):
    if (r,c,dr,dc) not in lookup:
        rr = r + dr
        cc = c + dc
        try:
            while seats[rr][cc] == '.':
                if rr == 0 or cc == 0:
                    raise 'blah'
                rr += dr
                cc += dc
        except:
            rr = 0
            cc = 0
        lookup[(r,c,dr,dc)] = (rr, cc)

    return lookup[(r,c,dr,dc)]

def step2(seats: List[List[str]]):
    new_seats = deepcopy(seats)
    for r in range(1, len(seats) - 1):
        for c in range(1, len(seats[r]) - 1):
            neighbors = [find_neighbors(seats, r, c, dr, dc) for dr,dc in itertools.product(range(-1, 2), range(-1, 2)) if not (dr == 0 and dc == 0)]
            neighbors = [seats[r][c] for r,c in neighbors if (r,c) != (0,0)]
            occupied_neighbors = neighbors.count('#')
            # print(occupied_neighbors)
            if seats[r][c] == 'L' and occupied_neighbors == 0:
                new_seats[r][c] = '#'
            elif seats[r][c] == '#' and occupied_neighbors >= 5:
                new_seats[r][c] = 'L'
    return new_seats

def run(inp: List[str]):
    seats = [list('.' + r.strip() + '.') for r in inp]
    seats.insert(0, ['.' for x in seats[0]])
    seats.append(['.' for x in seats[0]])

    new_seats = step(seats)
    while not eq(seats, new_seats):
        seats = new_seats
        new_seats = step(seats)
        # pp(new_seats)

    print(sum([r.count('#') for r in new_seats]))

    seats = [list('.' + r.strip() + '.') for r in inp]
    seats.insert(0, ['.' for x in seats[0]])
    seats.append(['.' for x in seats[0]])

    new_seats = step2(seats)
    # pp(new_seats)
    while not eq(seats, new_seats):
        seats = new_seats
        new_seats = step2(seats)
        # pp(new_seats)

    print(sum([r.count('#') for r in new_seats]))
