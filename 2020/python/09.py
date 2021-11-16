from collections import deque
from itertools import combinations
from typing import List

def getInput():
    with open("09.txt") as f:
        return [int(n.strip()) for n in f.readlines()]

def findFirstNumberNotCorrect(numbers: List[int]) -> int:
    preamble = deque(numbers[:25])
    for n in numbers[25:]:
        sumOfPreamble = list(map(lambda x: sum(x), combinations(preamble, 2)))
        if n not in sumOfPreamble:
            return n
        else:
            preamble.popleft()
            preamble.append(n)
    return 0

def minMaxOfcont(numbers, toFind):
    low, high = 0,1
    while high < len(numbers):
        if sum(numbers[low:high]) < toFind:
            high += 1
        elif sum(numbers[low:high]) > toFind:
            low += 1
        else:
            return min(numbers[low:high]) + max(numbers[low:high])
    return 0


def main():
    numbers = getInput()
    firstWeakness = findFirstNumberNotCorrect(numbers)
    print(f"Part 1: {firstWeakness}")
    print(f"Part 2: {minMaxOfcont(numbers, firstWeakness)}")

if __name__ == "__main__":
    main()
    