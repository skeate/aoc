from importlib import reload
from typing import List


def inc(pw: str) -> str:
    if pw == "":
        return ""
    if pw[-1] == "z":
        return inc(pw[:-1]) + "a"
    return pw[:-1] + chr(ord(pw[-1]) + 1)

pairs = [c + c for c in 'abcdefghjkmnpqrstuvwxyz']

def has_two_pairs(pw: str) -> bool:
    return 1 < len([p for p in pairs if p in pw])

def valid(pw: str):
    ints = [ord(c) for c in pw]

    return (
        not "i" in pw
        and not "o" in pw
        and not "l" in pw
        and has_two_pairs(pw)
        and any(
            [
                triple[0] + 2 == triple[1] + 1 == triple[2]
                for triple in [
                    (ints[i], ints[i + 1], ints[i + 2]) for i in range(len(ints) - 2)
                ]
            ]
        )
    )


def run(inp: List[str]):
    pw = inp[0].strip()
    while not valid(pw):
        pw = inc(pw)
    print(pw)
    pw = inc(pw)
    while not valid(pw):
        pw = inc(pw)
    print(pw)
