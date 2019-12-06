#Advent of Code - Day 08
from enum import Enum

def part1(inputs):
    isChildrenInfo = True
    isMetaHeader = False
    isMetaData = False

    childStack = []
    metaStack = []
    metaSum = 0

    for entry in inputs:
        if isChildrenInfo:
            isChildrenInfo = False
            isMetaHeader = True
            childStack.append(entry)
        elif isMetaHeader:
            isMetaHeader = False
            metaStack.append(entry)
            if childStack[-1] > 0:
                isChildrenInfo = True
            else:
                isMetaData = True
                childStack.pop(-1)
        elif isMetaData:
            metaStack[-1] -= 1
            metaSum += entry
            if metaStack[-1] == 0:
                metaStack.pop(-1)
                if len(childStack) > 0:
                    childStack[-1] -= 1
                    if childStack[-1] == 0:
                        childStack.pop(-1)
                    else:
                        isChildrenInfo = True
                        isMetaData = False

    return metaSum

class Node():
    def __init__(self):
        self.children = []
        self.metaData = []
        self.nodeValue = 0

class ParseState(Enum):
    childrenInfo = 0
    metaHeader = 1
    metaData = 2

def part2(inputs):
    root = None

    state = ParseState.childrenInfo

    childStack = []
    metaStack = []

    currentNode = None

    for entry in inputs:
        print(entry,state)
        if state == ParseState.childrenInfo:
            #If we are at the beginning, create root node
            if root == None:
                root = Node()
                currentNode = root
            #Append children nodes
            for i in range(entry):
                currentNode.children.append(Node())
                childStack.append(currentNode.children[i])
            #Switch state
            state = ParseState.metaHeader

        elif state == ParseState.metaHeader:
            #Create metaData list
            for i in range(entry):
                currentNode.metaData.append(-1)

            if len(currentNode.children) > 0:
                #take
                currentNode = childStack[-1]
                state = ParseState.childrenInfo
            else:
                state = ParseState.metaData
                childStack.pop(-1)

        elif state == ParseState.metaData:
            for i,c in enumerate(currentNode.metaData):
                if c == -1:
                    currentNode.metaData[i] = entry
                    break
            if currentNode.metaData.count(-1) > 0:
                state = ParseState.metaData
            else:
                if len(currentNode.children) == 0:
                    currentNode.nodeValue = sum(currentNode.metaData)
                    #print(currentNode.nodeValue)
                else:
                    childSum = 0
                    for c in currentNode.metaData:
                        if c <= len(currentNode.children):
                            childSum += currentNode.children[c-1].nodeValue
                    currentNode.nodeValue = childSum
                #Switch State

                currentNode = childStack[-1]
                if len(childStack) > 0:
                    state = ParseState.childrenInfo
                else:
                    state = ParseState.metaData


    return root.nodeValue


def main():
    inputs = open("../data/test08.txt").readline()
    inputs = list(map(int,inputs.strip().split(" ")))

    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))

main()
