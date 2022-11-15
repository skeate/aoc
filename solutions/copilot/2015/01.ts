export const run = (lines: string[]) => {
  // get the first line
  const line = lines[0]

  // set starting floor to 0
  let floor = 0

  // reduce over the characters in the line
  // ( => +1, ) => -1
  // and print the final floor
  console.log(line.split('').reduce((floor, char) => {
    if (char === '(') {
      return floor + 1
    } else {
      return floor - 1
    }
  }
  , floor))

  // find when the elevator first goes negative
  // and immediately print the index plus one
  console.log(line.split('').findIndex((char, index) => {
    if (char === '(') {
      floor++
    } else {
      floor--
    }

    return floor < 0
  }
  ) + 1)



}
