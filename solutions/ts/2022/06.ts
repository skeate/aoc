import * as fp from "fp-ts"
import * as lib from "../lib"

export const run = (lines: string[]) => {
  const cons = lines[0].split("")

  for (let i = 0; i < cons.length; i++) {
    const packet = cons.slice(i, i + 4)
    if (new Set(packet).size === 4) {
      console.log(i + 4)
      break
    }
  }

  for (let i = 0; i < cons.length; i++) {
    const packet = cons.slice(i, i + 14)
    if (new Set(packet).size === 14) {
      console.log(i + 14)
      break
    }
  }
}
