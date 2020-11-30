import re
from typing import List

def run(inp: List[str]):
    vowels = 'aeiou'

    vowels = re.compile(r"[aeiou].*[aeiou].*[aeiou]")
    doubled = re.compile(r"(.)\1")
    avoid = re.compile(r'(ab|cd|pq|xy)')
    print(len([s for s in inp if vowels.search(s) is not None and doubled.search(s) is not None and avoid.search(s) is None]))

    twice_no_overlap = re.compile(r'(..).*\1')
    betwixt = re.compile(r'(.).\1')

    print(len([s for s in inp if twice_no_overlap.search(s) is not None and betwixt.search(s) is not None]))
