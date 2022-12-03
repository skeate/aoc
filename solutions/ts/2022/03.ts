import * as fp from "fp-ts"
import { pipe } from "fp-ts/lib/function"
import * as lib from "../lib"

const prios = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".split("")

export const run = (lines: string[]) => {
  const p = pipe(
    lines,
    fp.readonlyArray.filter((s) => s.length > 0),
    fp.readonlyArray.map((s) => [
      s.slice(0, s.length / 2),
      s.slice(s.length / 2),
    ]),
    fp.readonlyArray.map(([a, b]) => [a.split(""), b.split("")]),
    fp.readonlyArray.map(
      ([a, b]) => fp.readonlyArray.intersection(fp.string.Eq)(a, b)[0]
    ),
    fp.readonlyArray.foldMap(fp.number.MonoidSum)((s) => prios.indexOf(s))
  )

  console.log(p)

  const p2 = pipe(
    lines,
    fp.readonlyArray.filter((s) => s.length > 0),
    fp.readonlyArray.map((s) => s.split("")),
    fp.readonlyArray.chunksOf(3),
    fp.readonlyArray.map(
      ([a, b, c]) =>
        fp.readonlyArray.intersection(fp.string.Eq)(
          a,
          fp.readonlyArray.intersection(fp.string.Eq)(b, c)
        )[0]
    ),
    fp.readonlyArray.foldMap(fp.number.MonoidSum)((s) => prios.indexOf(s))
  )

  console.log(p2)
}
