import * as lib from "../lib"

export const run = (lines: string[]) => {
  const elves: number[][] = lib.splitMap(lines, parseInt)

  const elfSums = elves.map(lib.sum).sort()
  const p1 = elfSums.at(-1)!
  console.log(p1)

  const p2 = p1 + elfSums.at(-2)! + elfSums.at(-3)!

  console.log(p2)
}
