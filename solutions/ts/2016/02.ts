import * as fp from "fp-ts"
import * as lib from "../lib"

enum Dir {
  Up,
  Right,
  Down,
  Left,
}

const pad = {
  1: [1, 2, 4, 1],
  2: [2, 3, 5, 1],
  3: [3, 3, 6, 2],
  4: [1, 5, 7, 4],
  5: [2, 6, 8, 4],
  6: [3, 6, 9, 5],
  7: [4, 8, 7, 7],
  8: [5, 9, 8, 7],
  9: [6, 9, 9, 8],
}

const map = {
  U: Dir.Up,
  R: Dir.Right,
  D: Dir.Down,
  L: Dir.Left,
}

const pad2: Record<string, string[]> = {
  1: ["1", "1", "3", "1"],
  2: ["2", "3", "6", "2"],
  3: ["1", "4", "7", "2"],
  4: ["4", "4", "8", "3"],
  5: ["5", "6", "5", "5"],
  6: ["2", "7", "A", "5"],
  7: ["3", "8", "B", "6"],
  8: ["4", "9", "C", "7"],
  9: ["9", "9", "9", "8"],
  A: ["6", "B", "A", "A"],
  B: ["7", "C", "D", "A"],
  C: ["8", "C", "C", "B"],
  D: ["B", "D", "D", "D"],
}

export const run = (lines: string[]) => {
  console.log(
    lines
      .filter((l) => l.length > 0)
      .map((l) =>
        l
          .split("")
          .map((c) => map[c as keyof typeof map])
          .reduce((p, c) => pad[p as keyof typeof pad][c], 5)
      )
      .join("")
  )

  console.log(
    lines
      .filter((l) => l.length > 0)
      .map((l) =>
        l
          .split("")
          .map((c) => map[c as keyof typeof map])
          .reduce((p, c) => pad2[p as keyof typeof pad2][c], "5")
      )
      .join("")
  )
}
