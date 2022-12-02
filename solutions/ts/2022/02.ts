import * as fp from "fp-ts"
import * as lib from "../lib"

const a_rock = "A"
const a_paper = "B"
const a_scissors = "C"

const calcWith =
  (
    b_rock: "X" | "Y" | "Z",
    b_paper: "X" | "Y" | "Z",
    b_scissors: "X" | "Y" | "Z"
  ) =>
  (game: string) => {
    if (game === "") return 0
    const [a, b] = game.split(" ")
    const a_wins =
      (a === a_rock && b === b_scissors) ||
      (a === a_paper && b === b_rock) ||
      (a === a_scissors && b === b_paper)
    const draw =
      (a === a_rock && b === b_rock) ||
      (a === a_paper && b === b_paper) ||
      (a === a_scissors && b === b_scissors)

    return (
      (b === b_rock ? 1 : b === b_paper ? 2 : 3) + (a_wins ? 0 : draw ? 3 : 6)
    )
  }

const loseDrawWin = (game: string) => {
  const [a, b] = game.split(" ")
  if (a === a_rock) {
    if (b === "X") return 0 + 3
    if (b === "Y") return 3 + 1
    if (b === "Z") return 6 + 2
  }
  if (a === a_paper) {
    if (b === "X") return 0 + 1
    if (b === "Y") return 3 + 2
    if (b === "Z") return 6 + 3
  }
  if (a === a_scissors) {
    if (b === "X") return 0 + 2
    if (b === "Y") return 3 + 3
    if (b === "Z") return 6 + 1
  }
  return 0
}

export const run = (lines: string[]) => {
  const score = lib.sum(lines.map(calcWith("X", "Y", "Z")))

  console.log(score)

  const score2 = lib.sum(lines.map(loseDrawWin))

  console.log(score2)
}
