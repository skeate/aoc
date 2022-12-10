import * as fp from "fp-ts"

export const gcd = (a: number, b: number): number => {
  if (b === 0) {
    return a
  }
  if (a === 0) {
    return b
  }
  if (a % 2 === 0 && b % 2 === 0) {
    return 2 * gcd(a / 2, b / 2)
  }
  if (a % 2 === 0) {
    return gcd(a / 2, b)
  }
  if (b % 2 === 0) {
    return gcd(a, b / 2)
  }
  return gcd(Math.abs(a - b), Math.min(a, b))
}

export const lcm = (a: number, b: number): number => {
  return (a * b) / gcd(a, b)
}

export const factors = (n: number): number[] => {
  const factors = [1]
  let divisor = 2

  while (n >= 2) {
    if (n % divisor === 0) {
      factors.push(divisor)
      n = n / divisor
    } else {
      divisor++
    }
  }

  return factors
}

const primes = [
  2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
  73, 79, 83, 89, 97,
]

const trialFactorization = (
  n: number
): [remaining: number, factors: number[]] => {
  const factors: number[] = []

  primes.forEach((p) => {
    while (n % p === 0) {
      factors.push(p)
      n = n / p
    }
  })

  return [n, factors]
}

const pollardRho = (n: number): number => {
  const f = (x: number): number => (x * x + 1) % n
  let y = Math.floor(1 + Math.random() * (n - 2))
  let m = Math.floor(1 + Math.random() * (n - 2))
  let g = 1
  let r = 1
  let q = 1
  let ys = y
  let x = y

  while (g === 1) {
    x = y
    for (let i = 0; i < r; i++) {
      y = f(y)
    }
    let k = 0
    while (k < r && g === 1) {
      ys = y
      for (let i = 0; i < Math.min(m, r - k); i++) {
        y = f(y)
        q = (q * Math.abs(x - y)) % n
      }
      g = gcd(q, n)
      k = k + m
    }
    r = r * 2
  }

  if (g === n) {
    do {
      ys = f(ys)
      g = gcd(Math.abs(x - ys), n)
    } while (g === 1)
  }

  return g
}

export const primeFactors = (n: number): number[] => {
  let factors: number[]
  ;[n, factors] = trialFactorization(n)

  while (n > 1) {
    const factor = pollardRho(n)
    factors.push(factor)
    n = n / factor
  }

  return factors
}

export const memoize = <A, B>(f: (a: A) => B): ((a: A) => B) => {
  const cache = new Map<A, B>()
  return (a: A): B => {
    if (cache.has(a)) {
      return cache.get(a)!
    }
    const b = f(a)
    cache.set(a, b)
    return b
  }
}

export function split(xs: string[], sep?: string): string[][]
export function split<A>(xs: A[], sep: A): A[][]
export function split(xs: string[], sep: string = ""): string[][] {
  const result: string[][] = []
  let current: string[] = []
  xs.forEach((x) => {
    if (x === sep) {
      result.push(current)
      current = []
    } else {
      current.push(x)
    }
  })
  result.push(current)
  return result
}

export const splitAt =
  (l: number) =>
  (s: string): Array<string> => {
    const ret: string[] = []
    for (let i = 0; i < s.length; i += l) {
      ret.push(s.slice(i, i + l))
    }
    return ret
  }

export function splitMap<A>(
  xs: string[],
  map: (x: string) => A,
  sep?: string
): A[][]
export function splitMap<A, B>(xs: A[], map: (x: A) => B, sep: A): B[][]
export function splitMap<A>(
  xs: string[],
  map: (x: string) => A,
  sep: string = ""
): A[][] {
  const result: A[][] = []
  let current: A[] = []
  xs.forEach((x) => {
    if (x === sep) {
      result.push(current)
      current = []
    } else {
      current.push(map(x))
    }
  })
  result.push(current)
  return result
}

export const sum = (xs: number[]): number => {
  return xs.reduce((a, b) => a + b, 0)
}

export function* permutations<A>(as: A[]): Generator<A[], void> {
  if (as.length === 0) {
    yield []
    return
  }

  for (let i = 0; i < as.length; i++) {
    const a = as[i]
    const rest = as.slice(0, i).concat(as.slice(i + 1))
    for (const perm of permutations(rest)) {
      yield [a, ...perm]
    }
  }
}

/**
 * Find all combinations of a given length from a list of elements.
 *
 * If the length is not specified, all combinations of all lengths are returned.
 */
export function* combinations<A>(
  as: A[],
  len: number = -1
): Generator<A[], void> {
  if (len > as.length) {
    return
  }
  if (as.length === 0 || len === 0) {
    yield []
    return
  }

  if (len === as.length) {
    yield as
    return
  }

  if (len === -1) {
    yield []
    for (let i = 1; i <= as.length; i++) {
      yield* combinations(as, i)
    }
    return
  }

  for (let i = 0; i < as.length; i++) {
    const a = as[i]
    const rest = as.slice(i + 1)
    for (const comb of combinations(rest, len - 1)) {
      yield [a, ...comb]
    }
  }
}

export const pairs = <A>(as: A[]): Generator<[A, A], void> =>
  combinations(as, 2) as Generator<[A, A], void>

export const tap: <A>(f: (a: A) => void) => (a: A) => A = (f) => (a) => {
  f(a)
  return a
}
