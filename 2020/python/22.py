

from typing import List, Tuple


def splitAndInt(l: str) -> List[int]:
    return list(map(lambda x: int(x), l.split("\n")[1:]))


def getInput() -> Tuple[List[int], List[int]]:
    with open("22.txt") as f:
        one, two = f.read().split("\n\n")
        return splitAndInt(one), splitAndInt(two)


def getScore(l) -> int:
    size = len(l)
    return sum([(size - i) * s for i, s in enumerate(l)])


def combat(playerOne: List[int], playerTwo: List[int]) -> Tuple[List[int], List[int]]:
    while len(playerTwo) > 0 and len(playerOne) > 0:
        one = playerOne.pop(0)
        two = playerTwo.pop(0)
        if one > two:
            playerOne.extend([one, two])
        else:
            playerTwo.extend([two, one])
    return playerOne, playerTwo


def makeKey(playerOne: List[int], playerTwo: List[int]) -> str:
    return ",".join(list(map(lambda x: str(x), playerOne))) + "-" + ",".join(list(map(lambda x: str(x), playerTwo)))


def recursiveCombat(playerOne: List[int], playerTwo: List[int]) -> Tuple[List[int], List[int]]:
    seen = set()
    while len(playerTwo) > 0 and len(playerOne) > 0:
        key = makeKey(playerTwo, playerTwo)
        if key in seen:
            return playerOne, []
        else:
            seen.add(key)

        one = playerOne.pop(0)
        two = playerTwo.pop(0)
        if one <= len(playerOne) and two <= len(playerTwo):
            oneSub, twoSub = recursiveCombat(playerOne[:one], playerTwo[:two])
            if len(oneSub) > len(twoSub):
                playerOne.extend([one, two])
            else:
                playerTwo.extend([two, one])
        elif one > two:
            playerOne.extend([one, two])
        else:
            playerTwo.extend([two, one])
    return playerOne, playerTwo


def main():
    playerOne, playerTwo = getInput()
    playerOneFinished, playerTwoFinished = combat(playerOne[:], playerTwo[:])
    print("Part 1: {}".format(
        max(getScore(playerOneFinished), getScore(playerTwoFinished))))

    playerOneRec, playerTwoRec = recursiveCombat(playerOne[:], playerTwo[:])
    print("Part 2: {}".format(max(getScore(playerOneRec), getScore(playerTwoRec))))


if __name__ == "__main__":
    main()
