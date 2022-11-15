from typing import List

def run(inp: List[str]):
    d = {
        parts[0]: {
            'speed': int(parts[3]),
            'time': int(parts[6]),
            'rest': int(parts[13])
        }
        for i in inp if (parts := i.split(' '))
    }
    distances = {
        rd: { 'dist': 0, 'to_go': rds['time'] - 1, 'points': 0 }
        for rd, rds in d.items()
    }
    for _ in range(2503):
        for rd, rds in d.items():
            distances[rd]['dist'] += rds['speed'] if distances[rd]['to_go'] >= 0 else 0
            if distances[rd]['to_go'] == -rds['rest']:
                distances[rd]['to_go'] = rds['time']
            distances[rd]['to_go'] -= 1
        lead = max(rd['dist'] for rd in distances.values())
        for rd in distances:
            if distances[rd]['dist'] == lead:
                distances[rd]['points'] += 1
    print(max(rd['dist'] for rd in distances.values()))
    print(max(rd['points'] for rd in distances.values()))
