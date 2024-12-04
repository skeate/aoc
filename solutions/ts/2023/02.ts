import * as fp from "fp-ts";
import * as lib from "../lib";

export const run = (lines: string[]) => {
  const parsedGames = lines
    .map(l => Array.from(/Game (\d+): (.*)/.exec(l)!))
    .map(([_, gameId, gameStats]) => [
      parseInt(gameId),
      gameStats
        .split('; ')
        .map((pull: string) =>
          fp.readonlyRecord.fromFoldable(
            fp.semigroup.last<number>(),
            fp.readonlyArray.Foldable
          )(
            pull
              .split(', ')
              .map(pair => fp.function.pipe(
                pair.split(' '),
                ([num, color]) => [color, parseInt(num)] as const
              ))
          )
        )
    ] as const)

  const part1 = parsedGames
    .filter(([_, draws]) => !draws.some(draw => (draw.red ?? 0) > 12 || (draw.green ?? 0) > 13 || (draw.blue ?? 0) > 14))
    .reduce((acc, [gameId]) => acc + gameId, 0)
  console.log(part1)

  const maxOfColor = (color: 'red' | 'green' | 'blue') => (draws: { red?: number, green?: number, blue?: number}[]): number => Math.max(...draws.map(d => d[color] ?? 0))

  const part2 = parsedGames
    .map(([_, draws]) => ({
      red: maxOfColor('red')(draws),
      green: maxOfColor('green')(draws),
      blue: maxOfColor('blue')(draws),
    }))
    .reduce((acc, colors) => acc + (colors.red * colors.green * colors.blue), 0)

  console.log(part2)
};
