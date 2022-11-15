from typing import List
from itertools import groupby, accumulate
from functools import reduce
import math

def extended_euclid_gcd(a, b):
    """
    Returns a list `result` of size 3 where:
    Referring to the equation ax + by = gcd(a, b)
        result[0] is gcd(a, b)
        result[1] is x
        result[2] is y 
    """
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a
    while r != 0:
        quotient = old_r//r
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
    return [old_r, old_s, old_t]


def combine_mods(a: (int, int), b: (int, int)):
    a1, n1 = a
    a2, n2 = b
    _gcd, m1, m2 = extended_euclid_gcd(n1, n2)
    return ((a1*m2*n2 + a2*m1*n1) % (n1*n2), n1*n2)

def scan(xs):
    return list(accumulate(xs))


def run(inp: List[str]):
    earliest = int(inp[0])
    buses = [int(b) for b in inp[1].split(',') if b != 'x']

    next_times = [(b - (earliest % b), b) for b in buses]
    first_after_earliest = min(next_times)
    print(first_after_earliest[0] * first_after_earliest[1])

    """
    Part 2 basically constructs a system of congruences, e.g.

    29,x,x,41,601 ->
    x := 0 mod 29
    x + 3 := 0 mod 41
    x + 4 := 0 mod 601

    shuffling things around so x is always on the left,
    x := 0 mod 29
    x := (-3 % 41) mod 41
    x := (-4 % 601) mod 601

    We can combine two congruencies using Bezout coefficients, yielding another
    conguence. Keep combining until we have one congruence, and the modulus is
    the answer.
    """
    with_skips = [b if b == 'x' else int(b) for b in inp[1].split(',')]
    counts = [(i, len(list(c))) for i, c in groupby(with_skips)]
    neg_skips = [0] + [1 + x[1] for x in counts if x[0] == 'x']
    congruences = [(-x[0] % x[1], x[1]) for x in zip(scan(neg_skips), buses)]

    final_mod = reduce(combine_mods, congruences)

    print(final_mod[0])
