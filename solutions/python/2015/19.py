import itertools
from typing import List
import heapq
from collections.abc import Callable
import editdistance


def levenshtein(s1: str):
    def r(s2: str):
        # calculate levenshtein distance between s1 and s2
        dist = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dist[0] = list(range(len(s2) + 1))
        for i in range(len(s1) + 1):
            dist[i][0] = i

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dist[i][j] = min(
                    dist[i - 1][j] + 1,
                    dist[i][j - 1] + 1,
                    dist[i - 1][j - 1] + (0 if s1[i - 1] == s2[j - 1] else 1)
                )
        return dist[-1][-1]
    return r


def astar(start, goal, get_neighbors: Callable[[str], List[str]], heuristic):
    nexts = [(heuristic(start), start, 0)]
    visited = set()
    max_dist = 0
    while len(nexts) > 0:
        h, n, d = heapq.heappop(nexts)
        max_dist = max(max_dist, d)
        visited.add(n)
        if n == goal:
            return d
        for nn in get_neighbors(n):
            if nn not in visited:
                heapq.heappush(nexts, (d + 1 + heuristic(nn), nn, d + 1))
    return None


def get_all_subs(replacements):
    def r(s):
        for r, n in replacements:
            i = 0
            while i != -1:
                i = s.find(r, i)
                if i != -1:
                    yield s[:i] + s[i:].replace(r, n, 1)
                    i += 1
    return r


def run(inp: List[str]):
    orig = inp[-1].strip()
    replacements = [s.strip().split(' => ') for s in inp[0:-2]]

    reps = get_all_subs(replacements)

    new_molecules = set(reps(orig))

    print(len(new_molecules))

    rev_replacements = [(n, r) for r, n in replacements]
    reps2 = get_all_subs(rev_replacements)

    print(astar(orig, 'e', reps2, lambda s: editdistance.eval(s, 'e')))
