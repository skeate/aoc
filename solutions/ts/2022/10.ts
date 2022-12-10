import { pipe } from "fp-ts/function"
import { Monoid } from "fp-ts/lib/string"
import * as RA from "fp-ts/ReadonlyArray"
import { splitAt } from "../lib"

export const run = (lines: string[]) => {
  const signalStrengths = pipe(
    lines,
    RA.foldMap(RA.getMonoid<number>())((s) =>
      s === "noop" ? [0] : [0, parseInt(s.slice(s.indexOf(" ") + 1), 10)]
    ),
    RA.scanLeft(1, (b, a) => b + a)
  )

  const toFind = [20, 60, 100, 140, 180, 220]

  console.log(
    toFind.reduce((acc, cur) => acc + cur * signalStrengths[cur - 1], 0)
  )

  const width = 40

  const output = pipe(
    signalStrengths.slice(0, -1),
    RA.foldMapWithIndex(Monoid)((i, a) =>
      a + 1 >= i % width && a - 1 <= i % width ? "\u2588" : " "
    ),
    splitAt(40),
    RA.intercalate(Monoid)("\n")
  )
  console.log(output)
}
