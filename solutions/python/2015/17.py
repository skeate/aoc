from itertools import combinations
from typing import List

def run(inp: List[str]):
    containers = [int(x.strip()) for x in inp]
    ways = 0
    min_containers = 100
    min_ways = 0
    for i in range(2, len(containers)):
        for combo in combinations(containers, i):
            if sum(combo) == 150:
                if min_containers == 100:
                    min_containers = i
                if min_containers == i:
                    min_ways += 1
                ways += 1
    print(ways)
    print(min_ways)
