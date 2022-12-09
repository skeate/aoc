import { flow, pipe } from "fp-ts/function"
import * as RA from "fp-ts/ReadonlyArray"
import * as RNEA from "fp-ts/ReadonlyNonEmptyArray"
import * as O from "fp-ts/Option"
import { isEmpty, split } from "fp-ts/lib/string"
import { not } from "fp-ts/lib/Predicate"

type Coord = { x: number; y: number }
type CoordHash = `${number},${number}`

const coord = (x: number, y: number): Coord => ({ x, y })
const hash = (c: Coord): CoordHash => `${c.x},${c.y}` as const

const dist2 = (a: Coord, b: Coord) => (a.x - b.x) ** 2 + (a.y - b.y) ** 2

type Rope = RNEA.ReadonlyNonEmptyArray<Coord>

const addc =
  (dx: number, dy: number) =>
  (c: Coord): Coord => ({
    x: c.x + dx,
    y: c.y + dy,
  })

const nudgeToward =
  (b: number) =>
  (a: number): number =>
    a === b ? a : b < a ? a - 1 : a + 1

const follow = (n: Coord, o: Coord): Coord =>
  // if dist2 < 4 (i.e. dist < 2) then we're already adjacent and don't need to move
  dist2(n, o) < 4 ? o : { x: nudgeToward(n.x)(o.x), y: nudgeToward(n.y)(o.y) }

const move: (dx: number, dy: number) => (r: Rope) => Rope =
  (dx, dy) =>
  ([h, ...knots]) =>
    pipe(
      knots,
      RA.scanLeft(addc(dx, dy)(h), follow),
      RNEA.fromReadonlyArray,
      O.getOrElse(() => pipe(RNEA.of(h), RNEA.concat(knots)))
    )

const dir = {
  L: move(-1, 0),
  R: move(1, 0),
  U: move(0, -1),
  D: move(0, 1),
}

export const run = (lines: string[]) => {
  const moves = pipe(
    lines,
    RA.filterMap(flow(O.fromPredicate(not(isEmpty)), O.map(split(" ")))),
    RA.chain(([d, c]) =>
      RNEA.replicate(dir[d as keyof typeof dir])(parseInt(c))
    )
  )

  const trackTail = (rope: Rope): Set<CoordHash> => {
    const tracker = new Set<CoordHash>()
    tracker.add(hash(RNEA.last(rope)))
    moves.reduce((r, f) => {
      const next = f(r)
      tracker.add(hash(RNEA.last(next)))
      return next
    }, rope)
    return tracker
  }

  console.log(trackTail(RNEA.replicate(coord(0, 0))(2)).size)
  console.log(trackTail(RNEA.replicate(coord(0, 0))(10)).size)
}
