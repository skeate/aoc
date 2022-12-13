import * as fp from "fp-ts"
import { filterMap, filterMapWithIndex } from "fp-ts/lib/Array"
import { flow, pipe } from "fp-ts/lib/function"
import { none, some } from "fp-ts/lib/Option"
import * as lib from "../lib"

type Signal = number | Array<Signal>
type SignalPair = [left: Array<Signal>, right: Array<Signal>]

export const run = (lines: string[]) => {
  const signals: Array<SignalPair> = lib
    .split(lines, "")
    .map((s) => s.map(eval)) as Array<SignalPair>

  const matchedIndices = pipe(
    signals,
    filterMapWithIndex((i, [left, right]) =>
      lesser(left, right) === "left" ? some(i + 1) : none
    )
  )

  console.log(lib.sum(matchedIndices))

  const two = [[2]]
  const six = [[6]]
  const allPackets = [...signals.flatMap((s) => s), two, six]

  allPackets.sort(
    flow(lesser, (l) => (l === "left" ? -1 : l === "right" ? 1 : 0))
  )

  const twoi = allPackets.indexOf(two) + 1
  const sixi = allPackets.indexOf(six) + 1

  console.log(twoi * sixi)
}

function lesser(
  left: Array<Signal>,
  right: Array<Signal>
): "left" | "right" | "equal" {
  let i = 0
  for (i = 0; i < left.length; i++) {
    const li = left[i]
    if (i >= right.length) return "right"
    const ri = right[i]
    let reit: "left" | "right" | "equal" = "equal"
    if (li instanceof Array && ri instanceof Array) {
      reit = lesser(li, ri)
    } else if (li instanceof Array) {
      reit = lesser(li, [ri])
    } else if (ri instanceof Array) {
      reit = lesser([li], ri)
    } else {
      reit = li < ri ? "left" : li > ri ? "right" : "equal"
    }
    if (reit !== "equal") {
      return reit
    }
  }

  if (i < right.length) return "left"

  return "equal"
}
