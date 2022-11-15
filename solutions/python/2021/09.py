from typing import List

def neighbors(x, y, width, height):
    if x == 0:
        xns = [(x + 1, y)]
    elif x == width - 1:
        xns = [(x-1, y)]
    else:
        xns = [(x+1, y), (x-1, y)]
    if y == 0:
        yns = [(x, y + 1)]
    elif y == height - 1:
        yns = [(x, y-1)]
    else:
        yns = [(x, y-1), (x, y+1)]
    return xns + yns

def basin_size(p, hm, width, height):
    visited = set()
    to_visit = [p]
    while len(to_visit) > 0:
        np = to_visit.pop()
        visited.add(np)
        for nx, ny in neighbors(np[0], np[1], width, height):
            if (nx,ny) not in visited and hm[ny][nx] != 9:
                to_visit.append((nx, ny))
    return len(visited)


def run(inp: List[str]):
    heightmap = [[int(h) for h in list(r.strip())] for r in inp]
    width = len(heightmap[0])
    height = len(heightmap)
    risks = 0
    low_points = []
    for y in range(height):
        for x in range(width):
            if all(heightmap[y][x] < heightmap[ny][nx] for nx,ny in neighbors(x,y,width,height)):
                risks += 1 + heightmap[y][x]
                low_points.append((x, y))
    print(risks)

    basins = []
    for lp in low_points:
        basins.append(basin_size(lp, heightmap, width, height))
    basins.sort()
    print(basins[-1] * basins[-2] * basins[-3])
