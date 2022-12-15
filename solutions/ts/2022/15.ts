import * as fp from "fp-ts"
import * as lib from "../lib"

export const run = (lines: string[]) => {
  const data = lines.map((l) => {
    const [, , sx, sy, , , , , bx, by] = l.split(" ")
    const p = {
      sx: parseInt(sx.slice(2, -1)),
      sy: parseInt(sy.slice(2, -1)),
      bx: parseInt(bx.slice(2, -1)),
      by: parseInt(by.slice(2)),
    }

    return {
      ...p,
      dist: lib.distManhattan([p.sx, p.sy], [p.bx, p.by]),
    }
  })

  const b2m = data.filter((d) => d.by === 2_000_000)

  let x = b2m[0].bx + 1
  let count = 0
  while (
    data.some((d) => lib.distManhattan([d.sx, d.sy], [x, 2_000_000]) <= d.dist)
  ) {
    x++
    count++
  }
  x = b2m[0].bx - 1
  while (
    data.some((d) => lib.distManhattan([d.sx, d.sy], [x, 2_000_000]) <= d.dist)
  ) {
    x--
    count++
  }

  console.log(count)

  // given that we know there is exactly one space in the region
  // which is not within the "closest beacon distance" of any of the sensors
  // we know that point must be at that distance + 1 of at least one sensor.
  // so we can sweep in a circle around each sensor, and check if the point
  // is outside the distance for all sensors. if so, it's where the hidden
  // beacon is.

  // for my input, this winds up checking 49347644 points (total; not counting
  // early termination), which 0.0003% of the brute force solution of checking
  // every point in the 4 million square grid.
  for (let i = 0; i < data.length; i++) {
    const { sx, sy, dist } = data[i]
    const outerRing = dist + 1
    for (let d = -outerRing; d <= outerRing; d++) {
      const y = sy + d
      const x1 = sx + (outerRing + d)
      const x2 = sx - (outerRing + d)

      if (y < 0 || y > 4_000_000) {
        continue
      }
      // lol
      for (let x = x1; x != x2; x = x2) {
        if (x >= 0 && x <= 4_000_000) {
          if (
            data.every((d) => lib.distManhattan([d.sx, d.sy], [x, y]) > d.dist)
          ) {
            console.log(x * 4_000_000 + y)
            return
          }
        }
      }
    }
  }
}
