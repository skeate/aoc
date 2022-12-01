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
  const factors = []
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
