export const run = (lines: string[]) => {
  const elves: number[][] = []
  let elf = 0

  lines.forEach((l) => {
    if (l === "") {
      elf++
    } else {
      elves[elf] = elves[elf] || []
      elves[elf].push(parseInt(l))
    }
  })

  const elfSums = elves.map((elf) => elf.reduce((a, b) => a + b, 0)).sort()
  console.log(elfSums[elfSums.length - 1])

  console.log(
    elfSums[elfSums.length - 1] +
      elfSums[elfSums.length - 2] +
      elfSums[elfSums.length - 3]
  )
}
