from copy import deepcopy
from typing import List

def get_boards(seq):
    return (seq[pos:pos + 5] for pos in range(0, len(seq), 6))

def mark_board(board, num):
    return [[str(x) if x == num else x for x in r] for r in board]

def mark_boards(boards, num):
    for b in range(len(boards)):
        boards[b] = mark_board(boards[b], num)

def check_board(board):
    if any(all(type(x) == str for x in r) for r in board):
        return True
    for i in range(5):
        if all(type(r[i]) == str for r in board):
            return True

def score_board(board):
    ret = sum(sum(x for x in r if type(x) != str) for r in board)
    return ret

def run(inp: List[str]):
    nums = [int(s) for s in inp[0].strip().split(',')]
    boards = [
        [
            [
                int(k) for k in z.strip().split(' ') if len(k) > 0
            ]
            for z in b
        ] for b in get_boards(inp[2:])
    ]

    def go():
        new_boards = deepcopy(boards)
        for num in nums:
            mark_boards(new_boards, num)
            for board in new_boards:
                if check_board(board):
                    print(score_board(board) * num)
                    return
    go()

    def go2():
        for num in nums:
            mark_boards(boards, num)
            for board in boards:
                if check_board(board):
                    if len(boards) == 1:
                        print(score_board(board) * num)
                    boards.remove(board)
    go2()
