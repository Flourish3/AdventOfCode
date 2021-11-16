from os import replace
from typing import List
from collections import deque


def getInput() -> List[str]:
    with open("05.txt") as f:
        return [s.strip().replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1") for s in f.readlines()]


def getRowOrColumn(ops: List[str]) -> int:
    min = 0
    max = 2 ** len(ops) - 1
    for op in ops:
        middle = (max-min) // 2 + min
        if op == "1":
            min = middle + 1
        else:
            max = middle
    return min


def getSeatId(seatCode: str) -> int:
    row, column = getRowOrColumn(
        list(seatCode[:7])), getRowOrColumn(list(seatCode[-3:]))
    return row * 8 + column


def main():
    lines = getInput()
    seatIds = sorted(list(map(lambda x: getSeatId(x), lines)))
    print("Part 1: {}".format(max(seatIds)))

    deq = deque(seatIds)
    deq.rotate(1)
    print("Part 2: {}".format([min(first, second) + 1 
                                for first,second in zip(seatIds, list(deq)) if abs(second - first) == 2][0]))


if __name__ == "__main__":
    main()
