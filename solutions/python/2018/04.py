import operator
import re
from typing import List

def run(inp: List[str]):
    inp.sort()
    current_guard = 0
    minutes = {}
    st = 0
    for event in inp:
        e = re.search(r'#(\d+)', event)
        if e is not None:
            current_guard = int(e.group(1))
        else:
            e = re.search(r'(\d+)] (f|w)', event)
            if e.group(2) == 'f':
                st = int(e.group(1))
            else:
                if current_guard not in minutes:
                    minutes[current_guard] = {}
                for m in range(st, int(e.group(1))):
                    if m not in minutes[current_guard]:
                        minutes[current_guard][m] = 0
                    minutes[current_guard][m] += 1
    guard, schedule = max(minutes.items(), key=lambda m: sum(m[1].values()))
    minute, times = max(schedule.items(), key=lambda m: m[1])
    print(guard * minute)

    guard, schedule = max(minutes.items(), key=lambda m: max(m[1].values()))
    minute, times = max(schedule.items(), key=lambda m: m[1])
    print(guard * minute)
