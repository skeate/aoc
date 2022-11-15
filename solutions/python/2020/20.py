from typing import List
from collections import Counter
from math import prod

def rotate_cw(tile):
    return [*map(list, zip(*tile[::-1]))]


def get_edges(tile):
    return [
        (
            tile[0],
            [c[-1] for c in tile],
            tile[-1],
            [c[0] for c in tile],
        ),
        (
            tile[-1],
            list(reversed([c[-1] for c in tile])),
            tile[0],
            list(reversed([c[0] for c in tile])),
        ),
        (
            list(reversed(tile[0])),
            [c[0] for c in tile],
            list(reversed(tile[-1])),
            [c[-1] for c in tile],
        ),
    ]


def to_digit(edge):
    return int(''.join('0' if c == '.' else '1' for c in edge), base=2)


def run(inp: List[str]):
    tiles = {}
    cur_tile_id = 0
    cur_tile = []
    for l in inp:
        if l.startswith('Tile '):
            cur_tile_id = int(l[5:9])
        elif l == '\n':
            tiles[cur_tile_id] = cur_tile
            cur_tile = []
        else:
            cur_tile.append(list(l.strip()))

    tiles_to_edges = {}
    edges_to_tile_ids = {}
    for id, tile in tiles.items():
        orientations = get_edges(tile)
        tiles_to_edges[id] = set()
        for o in orientations:
            for edge in o:
                en = to_digit(edge)
                if en not in edges_to_tile_ids:
                    edges_to_tile_ids[en] = set()
                edges_to_tile_ids[en].add(id)
                tiles_to_edges[id].add(en)
    edge_tiles = [list(e)[0] for e in edges_to_tile_ids.values() if len(e) == 1]
    c = Counter(edge_tiles)
    corners = [x[0] for x in c.most_common(4)]
    print(prod(corners))

    picture = [12 * [None] for _ in range(12)]
    picture[0][0] = corners[0]
    tiles_left = set(tiles.keys()) - set(corners[0])
    cx = 1
    cy = 0
    while len(tiles_left) > 0:
        picture[
        cx += 1
        if cx == len(picture):
            cx = 0
            cy += 1

