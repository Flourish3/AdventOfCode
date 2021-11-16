# Advent of code - day 22

import re
from collections import deque

shuffleProcess = [l.strip() for l in open("../data/input22.txt").readlines()]

cutReg = re.compile(r"cut (-?\d+)")
dealNew = re.compile(r"deal into new stack")
dealInc = re.compile(r'deal with increment (\d+)')

numCards = 10

def dealInc(cards, inc):
    tmpList = [0]*len(cards)
    index = 0
    for e in cards:
        tmpList[index] = e
        index = (index+inc) % numCards
    return deque(tmpList)

cards = deque(range(numCards))
for inst in shuffleProcess:
    if re.search(cutReg, inst):
         cards.rotate(-int(re.findall(cutReg, inst)[0]))
    elif re.search(r"deal into new stack", inst):
        cards.reverse()
    else:
        cards = dealInc(cards, int(re.findall(r'deal with increment (\d+)', inst)[0]))

print(cards)
#print("Part 1: {}".format(cards.index(2019)))

numCards = 119315717514047
shuffleTimes = 101741582076661

def reverseShuffling(index, length):
    revShuffle = shuffleProcess[:]
    revShuffle.reverse()
    initialIndex = index
    print("Initial: ", index)
    for inst in revShuffle:
        if re.search(cutReg, inst):
            cutNum = int(re.findall(cutReg, inst)[0])
            initialIndex = (initialIndex + cutNum) % length
        elif re.search(r"deal into new stack", inst):
           initialIndex = length - 1 - initialIndex
        else:
            incNum = int(re.findall(r'deal with increment (\d+)', inst)[0])
            initialIndex = (length - (incNum * initialIndex)) % length
        print(initialIndex)
    return initialIndex


print("Part 2: {}".format([reverseShuffling(i, 10) for i in range(10)]))

def solve(c, n, p, o=0, i=1):
    inv = lambda x: pow(x, c-2, c)
    for s in [s.split() for s in open('../data/input22.txt').readlines()]:
        if s[0] == 'cut':  o += i * int(s[-1])
        if s[1] == 'with': i *= inv(int(s[-1]))
        if s[1] == 'into': o -= i; i *= -1
    o *= inv(1-i); i = pow(i, n, c)
    return (p*i + (1-i)*o) % c

for x in [(10007,10005,2019), (119315717514047,101741582076661,2020)]:
    print(solve(*x))