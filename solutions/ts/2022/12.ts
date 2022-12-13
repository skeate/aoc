import * as lib from "../lib"
import { PriorityQueue } from "@datastructures-js/priority-queue"

const elevations = "abcdefghijklmnopqrstuvwxyz".split("")
const hash = ([x, y]: [number, number]) => `${x},${y}`
const tup = (x: number, y: number): [number, number] => [x, y]

export const run = (lines: string[]) => {
  let start: [number, number] = [0, 0]
  let end: [number, number] = [0, 0]

  const heightmap = lines.map((line, y) =>
    line.split("").map((c, x) => {
      if (c === "S") {
        start = [x, y]
        return 0
      }
      if (c === "E") {
        end = [x, y]
        return 25
      }
      return elevations.indexOf(c)
    })
  )

  const part1 = () => {
    const neighbors = ([x, y]: [number, number]): [number, number][] =>
      [tup(x - 1, y), tup(x + 1, y), tup(x, y - 1), tup(x, y + 1)]
        .filter(
          ([x, y]) =>
            x >= 0 && y >= 0 && x < heightmap[0].length && y < heightmap.length
        )
        .filter(([nx, ny]) => heightmap[ny][nx] < heightmap[y][x] + 2)

    const toVisit = new PriorityQueue<
      [number, [number, number], [number, number][]]
    >((a, b) => a[0] - b[0])
    const visited = new Set<string>()

    toVisit.push([lib.distManhattan(start, end), start, []])

    while (toVisit.size() > 0) {
      const [p, next, path] = toVisit.pop()
      if (visited.has(hash(next))) {
        continue
      }
      if (hash(next) === hash(end)) {
        console.log(path.length)
        break
      }

      visited.add(hash(next))

      const nexts = neighbors(next)
      nexts.forEach((n) => {
        if (!visited.has(hash(n))) {
          toVisit.push([p + lib.distManhattan(n, end), n, [...path, next]])
        }
      })
    }
  }

  const part2 = () => {
    const neighbors = ([x, y]: [number, number]): [number, number][] =>
      [tup(x - 1, y), tup(x + 1, y), tup(x, y - 1), tup(x, y + 1)]
        .filter(
          ([x, y]) =>
            x >= 0 && y >= 0 && x < heightmap[0].length && y < heightmap.length
        )
        .filter(([nx, ny]) => heightmap[ny][nx] > heightmap[y][x] - 2)

    const toVisit = new PriorityQueue<
      [number, [number, number], [number, number][]]
    >((a, b) => a[0] - b[0])
    const visited = new Set<string>()

    toVisit.push([0, end, []])

    while (toVisit.size() > 0) {
      const [p, next, path] = toVisit.pop()
      if (visited.has(hash(next))) {
        continue
      }
      if (heightmap[next[1]][next[0]] === 0) {
        console.log(path.length)
        break
      }

      visited.add(hash(next))

      const nexts = neighbors(next)
      nexts.forEach((n) => {
        if (!visited.has(hash(n))) {
          toVisit.push([p + 1, n, [...path, next]])
        }
      })
    }
  }

  part1()
  part2()
}
