import * as fp from "fp-ts"
import { pipe } from "fp-ts/lib/function"
import * as lib from "../lib"

const parse = (line: string) =>
  line.split(",").map((r) => r.split("-").map(Number))

export const run = (lines: string[]) => {
  const contained = pipe(
    lines,
    fp.array.filter((s) => s.length > 0),
    fp.array.map(parse),
    fp.array.filter(
      ([a, b]) =>
        (a[0] <= b[0] && a[1] >= b[1]) || (a[0] >= b[0] && a[1] <= b[1])
    )
  )
  console.log(contained.length)

  const anyoverlap = pipe(
    lines,
    fp.array.filter((s) => s.length > 0),
    fp.array.map(parse),
    fp.array.filter(
      ([a, b]) =>
        (a[0] <= b[0] && a[1] >= b[0]) ||
        (a[0] >= b[0] && a[1] <= b[0]) ||
        (a[0] <= b[1] && a[1] >= b[1]) ||
        (a[0] >= b[1] && a[1] <= b[1]) ||
        (a[0] <= b[0] && a[0] >= b[1]) ||
        (a[0] >= b[0] && a[0] <= b[1]) ||
        (a[1] <= b[0] && a[1] >= b[1]) ||
        (a[1] >= b[0] && a[1] <= b[1])
    )
  )
  console.log(anyoverlap.length)
}
