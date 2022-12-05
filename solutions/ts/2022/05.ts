import * as fp from "fp-ts"
import * as lib from "../lib"

export const part1 = (lines: string[]) => {
  const [stacks, instructions] = lib.split(lines)

  const stacksp: Record<string, string[]> = {}

  stacks.forEach((stack) => {
    for (let i = 1, p = 1; p < stack.length; i++, p += 4) {
      if (stack[p] !== " ") {
        if (!(i in stacksp)) {
          stacksp[i] = []
        }
        stacksp[i]!.unshift(stack[p])
      }
    }
  })

  for (let ins in instructions) {
    const [, count, , from, , to] = instructions[ins].split(" ")
    for (let i = 0; i < parseInt(count); i++) {
      stacksp[to].push(stacksp[from].pop()!)
    }
  }

  console.log(
    stacksp[1].at(-1)! +
      stacksp[2].at(-1)! +
      stacksp[3].at(-1)! +
      stacksp[4].at(-1)! +
      stacksp[5].at(-1)! +
      stacksp[6].at(-1)! +
      stacksp[7].at(-1)! +
      stacksp[8].at(-1)! +
      stacksp[9].at(-1)!
  )
}

export const part2 = (lines: string[]) => {
  const [stacks, instructions] = lib.split(lines)

  const stacksp: Record<string, string[]> = {}

  stacks.forEach((stack) => {
    for (let i = 1, p = 1; p < stack.length; i++, p += 4) {
      if (stack[p] !== " ") {
        if (!(i in stacksp)) {
          stacksp[i] = []
        }
        stacksp[i]!.unshift(stack[p])
      }
    }
  })

  for (let ins in instructions) {
    const [, count, , from, , to] = instructions[ins].split(" ")
    stacksp[to] = stacksp[to].concat(
      stacksp[from].splice(stacksp[from].length - parseInt(count))
    )
  }

  console.log(
    stacksp[1].at(-1)! +
      stacksp[2].at(-1)! +
      stacksp[3].at(-1)! +
      stacksp[4].at(-1)! +
      stacksp[5].at(-1)! +
      stacksp[6].at(-1)! +
      stacksp[7].at(-1)! +
      stacksp[8].at(-1)! +
      stacksp[9].at(-1)!
  )
}

export const run = (lines: string[]) => {
  part1(lines)
  part2(lines)
}
