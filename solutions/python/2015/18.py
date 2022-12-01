from copy import deepcopy
from typing import Callable, Generic, List, Tuple, TypeVar

T = TypeVar('T')


class Matrix(Generic[T]):
    def __init__(self, data: List[List[T]]):
        self.matrix = data
        self.width = len(data[0])
        self.height = len(data)

    def neighbors(self, p: Tuple[int, int]):
        x, y = p
        return [
            self.matrix[y + dy][x + dx]
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
            if (dy != 0 or dx != 0)
            and 0 <= y + dy < self.height
            and 0 <= x + dx < self.width
        ]

    def step(self, get_next_state: Callable[[List[T], T], T]):
        new_matrix = deepcopy(self.matrix)
        for y in range(self.height):
            for x in range(self.width):
                new_matrix[y][x] = get_next_state(
                    self.neighbors((x, y)), self.matrix[y][x])
        self.matrix = new_matrix

    def count(self, predicate: Callable[[T], bool]) -> int:
        c = 0
        for row in self.matrix:
            for col in row:
                if predicate(col):
                    c += 1
        return c

    def print(self):
        for row in self.matrix:
            print(''.join(str(c) for c in row))


def life_rules(neighbors: List[str], state: str) -> str:
    if state == '#':
        return '#' if neighbors.count('#') in [2, 3] else '.'
    return '#' if neighbors.count('#') == 3 else '.'


def run(inp: List[str]):
    life = Matrix([list(s.strip()) for s in inp])
    for _ in range(100):
        life.step(life_rules)
    print(life.count(lambda s: s == '#'))

    life = Matrix([list(s.strip()) for s in inp])
    life.matrix[0][0] = '#'
    life.matrix[99][0] = '#'
    life.matrix[0][99] = '#'
    life.matrix[99][99] = '#'
    for _ in range(100):
        life.step(life_rules)
        life.matrix[0][0] = '#'
        life.matrix[99][0] = '#'
        life.matrix[0][99] = '#'
        life.matrix[99][99] = '#'

    print(life.count(lambda s: s == '#'))
