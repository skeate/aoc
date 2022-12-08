import { pipe } from "fp-ts/lib/function"
import * as St from "fp-ts/State"
import * as RA from "fp-ts/ReadonlyArray"
import { match } from "@simspace/matchers"
import * as O from "fp-ts/Option"
import { Bounded, MonoidSum } from "fp-ts/lib/number"
import { min } from "fp-ts/lib/Monoid"
import { Kind, URIS } from "fp-ts/HKT"
import { altAll, Alternative1 } from "fp-ts/lib/Alternative"

type Dir = {
  type: "dir"
  name: string
  children: Record<string, Node>
  size: number
}
type File = { type: "file"; name: string; size: number }

type Node = Dir | File

const Dir = (name: string): Dir => ({
  type: "dir",
  name,
  children: {},
  get size() {
    return pipe(
      Object.values(this.children),
      RA.foldMap(MonoidSum)((n) => n.size)
    )
  },
})

const File = (name: string, size: number): File => ({
  type: "file",
  name,
  size,
})

type Line =
  | { tag: "cd"; dir: string }
  | { tag: "file"; name: string; size: number }
  | { tag: "dir"; name: string }

const parseLine = (line: string): O.Option<Line> =>
  line === ""
    ? O.none
    : line.startsWith("$ cd")
    ? O.some({ tag: "cd", dir: line.split(" ")[2] })
    : line.startsWith("$ ls")
    ? O.none
    : line.startsWith("dir ")
    ? O.some({ tag: "dir", name: line.split(" ")[1] })
    : O.some({
        tag: "file",
        name: line.split(" ")[1],
        size: parseInt(line.split(" ")[0]),
      })

type FSState = {
  curPath: string[]
  fs: Node
}

const extract: <F extends URIS>(
  F: Alternative1<F>
) => (pred: (n: Node) => boolean) => (n: Node) => Kind<F, Node> =
  (F) => (pred) => (n) => {
    const children =
      n.type === "dir"
        ? pipe(Object.values(n.children), RA.map(extract(F)(pred)), altAll(F))
        : F.zero<Node>()
    if (pred(n)) {
      return F.alt(children, () => F.of(n))
    }
    return children
  }

const getPath =
  (path: string[]) =>
  (fs: Node): Node =>
    path.reduce((fs, dir) => (fs.type === "dir" ? fs.children[dir] : fs), fs)

export const run = (lines: string[]) => {
  const fs = pipe(
    lines,
    RA.filterMap(parseLine),
    RA.traverse(St.Applicative)(
      match.w({
        cd: ({ dir }) =>
          St.modify<FSState>((s) => {
            let newPath: string[]
            if (dir === "/") {
              newPath = []
            } else if (dir === "..") {
              newPath = s.curPath.slice(0, s.curPath.length - 1)
            } else {
              newPath = [...s.curPath, dir]
            }
            return {
              curPath: newPath,
              fs: s.fs,
            }
          }),
        file: ({ name, size }) =>
          St.modify<FSState>((s) => {
            const curDir = getPath(s.curPath)(s.fs)
            if (curDir.type === "dir") {
              if (!(name in curDir.children)) {
                curDir.children[name] = File(name, size)
              }
            }
            return s
          }),
        dir: ({ name }) =>
          St.modify<FSState>((s) => {
            const curDir = getPath(s.curPath)(s.fs)
            if (curDir.type === "dir") {
              if (!(name in curDir.children)) {
                curDir.children[name] = Dir(name)
              }
            }
            return s
          }),
      })
    ),
    St.execute({
      curPath: [],
      fs: Dir(""),
    } as FSState),
    (x) => x.fs
  )

  const dirsWithSizeAtMost100000 = extract(RA.Alternative)(
    (n) => n.type === "dir" && n.size <= 100000
  )(fs)

  console.log(dirsWithSizeAtMost100000.reduce((acc, n) => acc + n.size, 0))

  const usedDiskSpace = fs.size
  const totalDiskSpace = 70_000_000
  const neededForUpdate = 30_000_000
  const needToClear = usedDiskSpace + neededForUpdate - totalDiskSpace

  const smallestBigEnough = pipe(
    extract(RA.Alternative)((n) => n.type === "dir" && n.size >= needToClear)(
      fs
    ),
    RA.foldMap(min(Bounded))((n) => n.size)
  )

  console.log(smallestBigEnough)
}
