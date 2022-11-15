from typing import List

def rotate_append(a, v):
    return a[1:] + [v]

def run(inp: List[str]):
    lf = list(map(int, inp[0].split(',')))

    number_added_by_day = {
        0: 0,
        1: lf.count(0),
        2: lf.count(1),
        3: lf.count(2),
        4: lf.count(3),
        5: lf.count(4),
        6: lf.count(5),
    }

    count = len(lf)

    addendum_queue = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(257):
        number_added_by_day[i % 7] += addendum_queue[0]
        new = number_added_by_day[i % 7]
        count += new
        addendum_queue = rotate_append(addendum_queue, new)
        if i == 80:
            print(count)
    print(count)
