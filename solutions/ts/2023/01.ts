import * as fp from "fp-ts";
import * as lib from "../lib";

const digitWords = {
  one: 1,
  two: 2,
  three: 3,
  four: 4,
  five: 5,
  six: 6,
  seven: 7,
  eight: 8,
  nine: 9,
}

const has = (x: string): x is keyof typeof digitWords => x in digitWords

export const run = (lines: string[]) => {
  const part1 = lines.map(l => Array.from(l.matchAll(/\d/g)))
    .map(digits => parseInt(`${digits[0]}${digits[digits.length-1]}`))
    .reduce((a, n) => a + n, 0)

  console.log(part1)

  const regex = `(?=(\\d|${Object.keys(digitWords).join('|')}))`
  const part2 = lines
    .map(l => [l, Array.from(l.matchAll(new RegExp(regex, 'g')))])
    .map(([l, matches]) => [l, [matches[0][1], matches[matches.length - 1][1]]] as const)
    .map(([l, r]) => [l, r.map(x => has(x) ? digitWords[x] : x)] as const)
    .map(([l, [first, last]]) => [l, parseInt(`${first}${last}`)] as const)
    .reduce((a, [_, n]) => a + n, 0)
  console.log(part2)
};
