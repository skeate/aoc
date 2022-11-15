from statistics import median
from typing import List

pairs = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>'
}

illegal_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

completion_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def illegal(s):
    expecteds = []
    for c in list(s):
        if c in pairs:
            expecteds.append(pairs[c])
        elif c == expecteds[-1]:
            expecteds.pop()
        else:
            return illegal_scores[c]
    return expecteds

def completion(s):
    score = 0
    for c in reversed(list(s)):
        score = score * 5 + completion_scores[c]
    return score

def run(inp: List[str]):
    result = [illegal(s.strip()) for s in inp]
    illegals = [x for x in result if type(x) is int]
    completions = [completion(x) for x in result if type(x) is not int]
    print(sum(illegals))
    print(median(completions))
