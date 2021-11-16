from functools import reduce
from collections import Counter
from typing import Set

def getInput():
    with open("10.txt") as f:
        joltList = [int(l.strip()) for l in f.readlines()]
        joltList.sort()
    return joltList

def getJoltDiff(joltList):
    return [joltList[i+1]-joltList[i] for i in range(len(joltList)-1)]

def traverseInfiniteTree(se: Set[int], n: int, maxi: int) -> int:
    if n + 3 == maxi:
        return 1
    else:
        return sum([traverseInfiniteTree(se, n + i, maxi) for i in [1,2,3] if n + i in se])

def getMultiPathCombinations(l):
    newL = [0]
    for i in range(len(l) - 1):
        if l[i+1] - l[i] == 3:
            newL.extend([l[i], l[i+1]])
    newL.append(l[-1])

    return newL

def getAllPossiblePaths(joltList):
    combinations = getMultiPathCombinations(joltList)

    return reduce(lambda a,b: a*b, [traverseInfiniteTree(set(joltList), combinations[i], combinations[i+1] + 3) for i in range(0, len(combinations), 2)])

def main():
    joltList = getInput()
    c = Counter(getJoltDiff(joltList))
    print(f"Part 1: {(c[1]+1) * (c[3]+1)}")
    print(f"Part 2: {getAllPossiblePaths(joltList)}")
    
if __name__ == "__main__":
    main()
