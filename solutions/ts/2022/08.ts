import * as fp from "fp-ts"
import * as lib from "../lib"

export const run = (lines: string[]) => {
  const matrix = lines
    .filter((s) => s !== "")
    .map((s) => s.split("").map((n) => parseInt(n)))

  const countViewFrom = (x: number, y: number) => {
    let count = 0
    let score = 1
    // up
    for (let i = y - 1; i >= 0; i--) {
      count++
      if (matrix[i][x] >= matrix[y][x]) break
    }
    score *= count
    count = 0
    // down
    for (let i = y + 1; i < matrix.length; i++) {
      count++
      if (matrix[i][x] >= matrix[y][x]) break
    }
    score *= count
    count = 0
    // left
    for (let i = x - 1; i >= 0; i--) {
      count++
      if (matrix[y][i] >= matrix[y][x]) break
    }
    score *= count
    count = 0
    // right
    for (let i = x + 1; i < matrix[0].length; i++) {
      count++
      if (matrix[y][i] >= matrix[y][x]) break
    }
    score *= count
    return score
  }

  const visible = new Set<string>()
  const add = (x: number, y: number) => {
    visible.add(`${x},${y}`)
  }
  // from left/right
  for (let y = 0; y < matrix.length; y++) {
    let highest = -1
    for (let x = 0; x < matrix[0].length; x++) {
      const tree = matrix[y][x]
      if (tree > highest) add(x, y)
      highest = Math.max(highest, tree)
    }

    highest = -1
    for (let x = matrix[0].length - 1; x >= 0; x--) {
      const tree = matrix[y][x]
      if (tree > highest) add(x, y)
      highest = Math.max(highest, tree)
    }
  }
  // from top/bottom
  for (let x = 0; x < matrix[0].length; x++) {
    let highest = -1
    for (let y = 0; y < matrix.length; y++) {
      const tree = matrix[y][x]
      if (tree > highest) add(x, y)
      highest = Math.max(highest, tree)
    }

    highest = -1
    for (let y = matrix.length - 1; y >= 0; y--) {
      const tree = matrix[y][x]
      if (tree > highest) add(x, y)
      highest = Math.max(highest, tree)
    }
  }

  console.log(visible.size)

  let bestViewCount = 0
  for (let y = 0; y < matrix.length; y++) {
    for (let x = 0; x < matrix[0].length; x++) {
      const viewCount = countViewFrom(x, y)
      if (viewCount > bestViewCount) {
        bestViewCount = viewCount
      }
    }
  }

  console.log(bestViewCount)
}
