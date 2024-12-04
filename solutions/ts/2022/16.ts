import { number } from "fp-ts"
import { pipe } from "fp-ts/lib/function"
import * as RA from "fp-ts/lib/ReadonlyArray"
import * as RR from "fp-ts/lib/ReadonlyRecord"
import * as Sg from "fp-ts/lib/Semigroup"
import * as lib from "../lib"

export const run = (lines: string[]) => {
  const valves = RR.fromFoldableMap(
    Sg.last<{ rate: number; connections: ReadonlyArray<string> }>(),
    RA.Foldable
  )(lines, (line) => {
    const [, n, , , rate_, , , , , ...connections_] = line.split(" ")
    const rate = parseInt(rate_.split("=")[1])
    const connections = connections_.map((c) => c.substring(0, 2))

    return [n, { rate, connections }]
  })

  
}
