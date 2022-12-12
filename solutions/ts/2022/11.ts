import * as fp from "fp-ts"
import { pipe } from "fp-ts/lib/function"
import * as lib from "../lib"

interface Monkey {
  items: { n: number }[]
  operation: (old: number) => number
  throwTo: (n: number) => number
  division: number
  inspected: number
}

const div3 = (n: number) => Math.floor(n / 3)

const getOperation = ([op, amt]: [string, string]) =>
  op === "*"
    ? (n: number) => n * (amt === "old" ? n : Number(amt))
    : (n: number) => n + (amt === "old" ? n : Number(amt))

const parseMonkey = (monkey: string[]): Monkey => {
  const items = monkey[1]
    .split(":")[1]
    .split(",")
    .map((n) => ({ n: Number(n) }))
  const operation = getOperation(
    monkey[2].split("=")[1].slice(5).split(" ") as [string, string]
  )
  const cond = Number(monkey[3].split("by")[1])
  const ifTrue = Number(monkey[4].split("monkey")[1])
  const ifFalse = Number(monkey[5].split("monkey")[1])
  const throwTo = (n: number) => (n % cond === 0 ? ifTrue : ifFalse)

  return {
    items,
    operation,
    throwTo,
    division: cond,
    inspected: 0,
  }
}

const part1 = (lines: string[]) => {
  const monkeys = pipe(lib.split(lines, ""), fp.array.map(parseMonkey))

  for (let i = 0; i < 20; i++) {
    monkeys.forEach((monkey, m) => {
      monkey.inspected += monkey.items.length
      while (monkey.items.length > 0) {
        const item = monkey.items.shift()!
        item.n = div3(monkey.operation(item.n))
        const to = monkey.throwTo(item.n)
        monkeys[to].items.push(item)
      }
    })
  }

  const inspectedCounts = monkeys.map((m) => m.inspected)

  console.log(lib.product(lib.top(2)(inspectedCounts)))
}

const part2 = (lines: string[]) => {
  const monkeys = pipe(lib.split(lines, ""), fp.array.map(parseMonkey))

  const prod_of_divis = monkeys.map((m) => m.division).reduce((a, b) => a * b)

  for (let i = 0; i < 10000; i++) {
    monkeys.forEach((monkey, m) => {
      monkey.inspected += monkey.items.length
      while (monkey.items.length > 0) {
        const item = monkey.items.shift()!
        item.n = monkey.operation(item.n) % prod_of_divis
        const to = monkey.throwTo(item.n)
        monkeys[to].items.push(item)
      }
    })
  }

  const inspectedCounts = monkeys.map((m) => m.inspected)

  console.log(lib.product(lib.top(2)(inspectedCounts)))
}

export const run = (lines: string[]) => {
  part1(lines)
  part2(lines)
}
