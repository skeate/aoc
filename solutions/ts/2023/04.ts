import * as fp from "fp-ts";
import * as lib from "../lib";

export const run = (lines: string[]) => {
  const parsed = lines
    .map(l => /Card +(\d+): (.*?) \| (.*)/.exec(l))
    .flatMap(l => l ? [Array.from(l)] : [])
    .map(([_, id, winning, onCard]) => ({
      id,
      winning: new Set(winning.split(' ').flatMap(s => s.length ? [parseInt(s)] : [])),
      onCard: new Set(onCard.split(' ').flatMap(s => s.length ? [parseInt(s)] : [])),
    }))

  const part1 = parsed
    .map(({ winning, onCard }) => fp.set.intersection(fp.number.Eq)(winning, onCard).size)
    .map(wins => wins > 0 ? (2 ** (wins - 1)) : 0)
    .reduce((a, n) => a+n, 0)

  console.log(part1)

  const part2 = parsed
    .
};
