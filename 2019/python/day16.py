# Advent of code - day 16
import numpy as np
import math
from collections import deque

inputSequence = list(map(lambda c: int(c),list(open("../data/input16.txt").readline().strip())))

basePattern = [0, 1, 0, -1]
def generatePattern(index, length):
    retArr = []
    for i in range(len(basePattern)):
        for j in range(index + 1):
            retArr.append(basePattern[i])
    while len(retArr) <= length:
        retArr = retArr * 2

    return np.array(retArr[1:length+1])

# For 100 phases
output = inputSequence[:]
patterns = np.array([generatePattern(i, len(output)) for i in range(len(output))])
for i in range(100):
    
    output = list(map(lambda x: abs(x) % 10, np.dot(patterns, output)))

print("Part1: ", "".join(list(map(lambda x: str(x),output[:8]))))

# For 100 phases * 10'000
offset = (inputSequence[:7] * 10 ** np.arange(6,-1,-1)).sum()
output = np.tile(inputSequence[:],10000)[offset:]

for _ in range(100):
    output = np.cumsum(output[::-1])[::-1] % 10

print("Part2: ", "".join(list(map(lambda x: str(x),output[:8]))))