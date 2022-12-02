import * as fp from "fp-ts"
import { flow, pipe } from "fp-ts/lib/function"
import { concatAll } from "fp-ts/lib/Monoid"
import { MonoidSum } from "fp-ts/lib/number"
import * as O from "fp-ts/lib/Option"
import { filter, filterMap, map, sequence } from "fp-ts/lib/ReadonlyArray"
import * as lib from "../lib"

enum RPS {
  Rock,
  Paper,
  Scissors,
}

type Game = [opp: RPS, self: RPS]

const beats = {
  [RPS.Rock]: RPS.Paper,
  [RPS.Paper]: RPS.Scissors,
  [RPS.Scissors]: RPS.Rock,
}

const isBeatBy = {
  [RPS.Rock]: RPS.Scissors,
  [RPS.Paper]: RPS.Rock,
  [RPS.Scissors]: RPS.Paper,
}

const value = {
  [RPS.Rock]: 1,
  [RPS.Paper]: 2,
  [RPS.Scissors]: 3,
}

const score = ([p1, p2]: Game) => {
  const playedScore = value[p2]
  const winScore = p2 === beats[p1] ? 6 : 0
  const drawScore = p1 === p2 ? 3 : 0
  return playedScore + winScore + drawScore
}

const parsep1 = (s: string): O.Option<RPS> =>
  s === "A"
    ? O.some(RPS.Rock)
    : s === "B"
    ? O.some(RPS.Paper)
    : s === "C"
    ? O.some(RPS.Scissors)
    : O.none

const parseGame1 = (s: unknown): O.Option<Game> => {
  if (typeof s !== "string" || s === "") return O.none
  const [p1, p2] = s.split(" ")
  const p1p = parsep1(p1)
  const p2p =
    p2 === "X"
      ? O.some(RPS.Rock)
      : p2 === "Y"
      ? O.some(RPS.Paper)
      : p2 === "Z"
      ? O.some(RPS.Scissors)
      : O.none
  return sequence(O.Applicative)([p1p, p2p]) as O.Option<Game>
}

const parseGame2 = (s: unknown): O.Option<Game> => {
  if (typeof s !== "string" || s === "") return O.none
  const [p1, p2] = s.split(" ")
  const p1p = parsep1(p1)
  const p2p = pipe(
    p1p,
    O.map((op) => (p2 === "X" ? isBeatBy[op] : p2 === "Y" ? op : beats[op]))
  )
  return sequence(O.Applicative)([p1p, p2p]) as O.Option<Game>
}

const printScore = (
  parser: (s: unknown) => O.Option<Game>
): ((s: string[]) => void) =>
  flow(
    filterMap(parser),
    map(score),
    concatAll(MonoidSum),
    console.log.bind(console)
  )

export const run: (lines: string[]) => void = flow(
  lib.tap(printScore(parseGame1)),
  lib.tap(printScore(parseGame2))
)
