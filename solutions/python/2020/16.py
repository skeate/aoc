from typing import List
from math import prod
import re


def prune(poses):
    iterate = False
    for i, p in enumerate(poses):
        if len(p) == 1:
            for j, p2 in enumerate(poses):
                if i != j and p.issubset(p2):
                    p2 -= p
                    iterate = True
    if iterate:
        prune(poses)


def run(inp: List[str]):
    re_valid = re.compile(r'([a-z][a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)')
    re_my_ticket = re.compile(r'your ticket: ((\d+,)+\d+)')
    re_nearby_tickets = re.compile(r'nearby tickets: ((\d+[, ])+\d+)')

    inp = ' '.join([l.strip() for l in inp])

    valid = {tag: (int(n1), int(x1), int(n2), int(x2)) for tag,n1,x1,n2,x2 in re_valid.findall(inp)}
    nearby_tickets = [tuple(map(int, t.split(','))) for t in re_nearby_tickets.findall(inp)[0][0].split(' ')]
    invalid = [(t, x) for t in nearby_tickets for x in t if not any(n1 <= x <= x1 or n2 <= x <= x2 for n1,x1,n2,x2 in valid.values())]
    print(sum(i[1] for i in invalid))
    invalid = set(i[0] for i in invalid)

    tickets = set(nearby_tickets) - invalid
    all_regions = set(valid.keys())
    poses = []
    for _ in nearby_tickets[0]:
        poses.append(all_regions.copy())
    for ticket in tickets:
        for vks, t in zip(poses, ticket):
            ivks = []
            for vk in vks:
                v = valid[vk]
                if not (v[0] <= t <= v[1] or v[2] <= t <= v[3]):
                    ivks.append(vk)
            vks -= set(ivks)
        prune(poses)
        if all(len(ps) == 1 for ps in poses):
            break
    poses = [list(p)[0] for p in poses]
    my_ticket = tuple(map(int, re_my_ticket.findall(inp)[0][0].split(',')))
    departures = [x if p.startswith('departure') else 1 for p,x in zip(poses,my_ticket)]
    print(prod(departures))
