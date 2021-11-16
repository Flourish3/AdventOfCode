import re
from typing import Dict

class BagInfo():
    def __init__(self, inputString) -> None:
        self.color = inputString[2:]
        self.number = int(inputString[0])

bagPattern = re.compile("(\d \w* \w*)")
mainBagPattern = re.compile("^(\w* \w*) bags")
def readInput():
    with open("07.txt") as f:
        return {re.match(mainBagPattern, l).groups()[0]: list(map(lambda x: BagInfo(x), re.findall(bagPattern, l))) for l in f.readlines()}

def findNumberForColor(dic: Dict, color):
    hasDirectly = [k for k,v in dic.items() if color in list(map(lambda x: x.color, v))]
    hasIndirectly = [findNumberForColor(dic, c) for c in hasDirectly]
    flatList = [item for sublist in hasIndirectly for item in sublist]
    hasDirectly.extend(flatList)

    return list(set(hasDirectly))

def findNumberOfBagsForColor(dic: Dict, color: str, multi: int):
    otherColors = sum(list(map(lambda x: findNumberOfBagsForColor(dic, x.color, x.number), dic[color])))
    return multi *(otherColors +  sum(list(map(lambda i: i.number, dic[color]))))

def main():
    inputDict = readInput()
    print("Part 1 {}".format(len(findNumberForColor(inputDict, "shiny gold"))))
    print("Part 2 {}".format(findNumberOfBagsForColor(inputDict, "shiny gold", 1)))

if __name__ == "__main__":
    main()

