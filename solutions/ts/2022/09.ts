import * as fp from "fp-ts"
import { pipe } from "fp-ts/lib/function"
import * as lib from "../lib"

type Coord = `${number},${number}`

const dist = (a: readonly [number, number], b: readonly [number, number]) =>
  (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

const part1 = (lines: string[]) => {
  type Pos = {
    head: readonly [number, number]
    tail: readonly [number, number]
  }
  const pos: Pos = {
    head: [0, 0],
    tail: [0, 0],
  }

  const move =
    (dx: number, dy: number) =>
    (pos: Pos): Pos => {
      const [x, y] = pos.head
      const [x2, y2] = pos.tail
      return {
        head: [x + dx, y + dy],
        tail: dist([x + dx, y + dy], pos.tail) < 4 ? [x2, y2] : [x, y],
      }
    }

  const right = move(-1, 0)
  const left = move(1, 0)
  const up = move(0, -1)
  const down = move(0, 1)

  const tailVisited = new Set<Coord>()

  const final = lines
    .filter((l) => l !== "")
    .flatMap((l) => {
      const [d, c] = l.split(" ")
      switch (d) {
        case "L":
          return fp.array.replicate(parseInt(c), left)
        case "R":
          return fp.array.replicate(parseInt(c), right)
        case "U":
          return fp.array.replicate(parseInt(c), up)
        case "D":
          return fp.array.replicate(parseInt(c), down)
        default:
          return []
      }
    })
    .reduce((pos, f) => {
      tailVisited.add(`${pos.tail[0]},${pos.tail[1]}` as Coord)
      return f(pos)
    }, pos)
  tailVisited.add(`${final.tail[0]},${final.tail[1]}` as Coord)

  console.log(tailVisited.size)
}

const part2 = (lines: string[]) => {
  type Pos = {
    head: readonly [number, number]
    tails: Array<readonly [number, number]>
  }

  const pos: Pos = {
    head: [0, 0],
    tails: fp.array.replicate(9, [0, 0]),
  }

  const move =
    (dx: number, dy: number) =>
    (pos: Pos): Pos => {
      const [x, y] = pos.head
      const head = [x + dx, y + dy] as const
      const tails = []
      let curHead = head
      let curPast = [x, y] as const
      for (let i = 0; i < pos.tails.length; i++) {
        const tail = pos.tails[i]
        if (dist(curHead, tail) < 4) {
          tails.push(...pos.tails.slice(i))
          break
        } else {
          tails.push(curPast)
          curHead = curPast
          curPast = tail
        }
      }

      return { head, tails }
    }

  const right = move(1, 0)
  const left = move(-1, 0)
  const up = move(0, -1)
  const down = move(0, 1)

  const tailVisited = new Set<Coord>()

  const final = lines
    .filter((l) => l !== "")
    .flatMap((l) => {
      const [d, c] = l.split(" ")
      switch (d) {
        case "L":
          return fp.array.replicate(parseInt(c), left)
        case "R":
          return fp.array.replicate(parseInt(c), right)
        case "U":
          return fp.array.replicate(parseInt(c), up)
        case "D":
          return fp.array.replicate(parseInt(c), down)
        default:
          return []
      }
    })
    .reduce((pos, f, i) => {
      tailVisited.add(`${pos.tails[8][0]},${pos.tails[8][1]}` as Coord)
      return f(pos)
    }, pos)
  tailVisited.add(`${final.tails[8][0]},${final.tails[8][1]}` as Coord)

  console.log(tailVisited.size)
}

export const run = (lines: string[]) => {
  part1(lines)
  part2(lines)
}
