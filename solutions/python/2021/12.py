from typing import List
from functools import cache

edges: dict[str, set[str]] = {}


@cache
def count_paths(start: str, end: str, visitable: frozenset[str]):
    nexts = edges[start] & visitable
    if len(nexts) == 0:
        return 0
    return sum(
        1
        if n == end
        else count_paths(n, end, visitable - {n} if n == n.lower() else visitable)
        for n in nexts
    )


@cache
def count_paths2(
    start: str,
    end: str,
    visitable: frozenset[str],
    visited_small_twice: bool = False,
    visited: frozenset[str] = frozenset()
):
    nexts = edges[start] & visitable
    if len(nexts) == 0:
        return 0
    return sum(
        1
        if n == end
        else count_paths2(
            n,
            end,
            (visitable - {n} - (visited if n in visited else frozenset())) if (n == n.lower() and (visited_small_twice or n in visited)) else visitable,
            visited_small_twice or (n == n.lower() and n in visited),
            (visited | {n}) if n == n.lower() else visited
        )
        for n in nexts
    )


@cache
def count_paths3(
    start: str,
    end: str,
    visitable: frozenset[str],
    visited_small_twice: bool = False,
    visited: frozenset[str] = frozenset(),
) -> List[List[str]]:
    nexts = edges[start] & visitable
    if len(nexts) == 0:
        return []
    return [
        item
        for sublist in (
            [[start] + [n]]
            if n == end
            else [
                [start] + p
                for p in count_paths3(
                    n,
                    end,
                    (visitable - {n} - (visited if n in visited else frozenset())) if (n == n.lower() and (visited_small_twice or n in visited)) else visitable,
                    visited_small_twice or (n == n.lower() and n in visited),
                    (visited | {n}) if n == n.lower() else visited
                )
            ]
            for n in nexts
        )
        for item in sublist
    ]


def run(inp: List[str]):
    edges_ = [set(r.strip().split("-")) for r in inp]
    nodes = frozenset(set.union(*edges_))
    for edge in edges_:
        e = list(edge)
        if e[0] not in edges:
            edges[e[0]] = set()
        if e[1] not in edges:
            edges[e[1]] = set()
        edges[e[0]].add(e[1])
        edges[e[1]].add(e[0])

    print(count_paths("start", "end", nodes - {"start"}))
    print(count_paths2("start", "end", nodes - {"start"}))
    # print(
    #     "\n".join(
    #         list(
    #             sorted(
    #             ",".join(p) 
    #             for p in count_paths3(
    #                 "start", "end", nodes - {"start"}
    #             ))
    #         )
    #     )
    # )
