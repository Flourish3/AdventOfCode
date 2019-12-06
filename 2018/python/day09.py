#Advent of Code - Day 09
from collections import defaultdict

class Node():
    def __init__(self, clockwise, counterClockwise, value):
        self.clockwise = clockwise
        self.counterClockwise = counterClockwise
        self.value = value

def solve(players, lastMarble):
    elves = defaultdict(int)

    currentNode = Node(None,None, 0)
    firstNode = Node(None,None, 1)

    currentNode.clockwise = firstNode
    currentNode.counterClockwise = firstNode

    firstNode.clockwise = currentNode
    firstNode.counterClockwise = currentNode

    currentNode = firstNode

    currentPlayer = 2

    for marbleNum in range(2,lastMarble+1):
        if marbleNum % 23 == 0:
            elves[currentPlayer] += marbleNum
            for i in range(7):
                currentNode = currentNode.counterClockwise
            elves[currentPlayer] += currentNode.value

            currentNode.counterClockwise.clockwise = currentNode.clockwise
            currentNode.clockwise.counterClockwise = currentNode.counterClockwise
            currentNode = currentNode.clockwise
        else:
            newCounterClockWise = currentNode.clockwise
            newClockwise = currentNode.clockwise.clockwise
            newNode = Node(newClockwise, newCounterClockWise, marbleNum)

            newCounterClockWise.clockwise = newNode
            newClockwise.counterClockwise = newNode

            currentNode = newNode

        currentPlayer = (currentPlayer + 1) % players

    maxScore = 0
    for k,v in elves.items():
        maxScore = max(maxScore, v)

    return maxScore


def main():
    players = 9
    lastMarble = 25
    print("Test 1: {}, should be {}".format(solve(players, lastMarble), 32))

    players = 13
    lastMarble = 7999
    print("Test 2: {}, should be {}".format(solve(players, lastMarble), 146373))

    players = 10
    lastMarble = 1618
    print("Test 3: {}, should be {}".format(solve(players, lastMarble), 8317))

    players = 17
    lastMarble = 1104
    print("Test 4: {}, should be {}".format(solve(players, lastMarble), 2764))

    players = 21
    lastMarble = 6111
    print("Test 5: {}, should be {}".format(solve(players, lastMarble), 54718))

    players = 30
    lastMarble = 5807
    print("Test 6: {}, should be {}".format(solve(players, lastMarble), 37305))

    players = 427
    lastMarble = 70723
    print("Part 1: {}".format(solve(players, lastMarble)))

    lastMarble *= 100
    print("Part 2: {}".format(solve(players, lastMarble)))

main()
