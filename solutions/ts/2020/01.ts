export const run = (lines: string[]) => {
  const ns = new Set(lines.map((l) => parseInt(l, 10)))

  let p1 = 0
  let p2 = 0

  for (const i of ns) {
    if (ns.has(2020 - i)) p1 = i * (2020 - i)
    for (const j of ns) {
      if (ns.has(2020 - i - j)) p2 = i * j * (2020 - i - j)
      if (p1 && p2) break
    }
    if (p1 && p2) break
  }
  console.log(p1)
  console.log(p2)
}
