import { pipe } from "fp-ts/function"
import * as RA from "fp-ts/ReadonlyArray"
import * as N from "fp-ts/number"
import * as Str from "fp-ts/string"
import { not } from "fp-ts/lib/Predicate"

const prios = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".split("")

export const run = (lines: string[]) => {
  const p = pipe(
    lines,
    RA.filter(not(Str.isEmpty)),
    RA.map(Str.split("")),
    RA.map((s) => [s.slice(0, s.length / 2), s.slice(s.length / 2)]),
    RA.map(([a, b]) => RA.intersection(Str.Eq)(a, b)[0]),
    RA.foldMap(N.MonoidSum)((s) => prios.indexOf(s))
  )

  console.log(p)

  const p2 = pipe(
    lines,
    RA.filter(not(Str.isEmpty)),
    RA.map(Str.split("")),
    RA.chunksOf(3),
    RA.map(
      ([a, b, c]) =>
        RA.intersection(Str.Eq)(a, RA.intersection(Str.Eq)(b, c))[0]
    ),
    RA.foldMap(N.MonoidSum)((s) => prios.indexOf(s))
  )

  console.log(p2)
}
