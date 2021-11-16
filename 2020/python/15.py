from typing import List


def runGame(initial: List[int], iterations: int) -> int:
    numbers = {i: [idx+1, 0] for idx, i in enumerate(initial)}
    lastNum = initial[-1]
    for i in range(len(initial)+1, iterations + 1):

        if numbers[lastNum][1] == 0:
            lastNum = 0
        else:
            lastNum = sum(numbers[lastNum])

        if lastNum in numbers:
            numbers[lastNum] = [i, -numbers[lastNum][0]]
        else:
            numbers[lastNum] = [i, 0]
    return lastNum


def main():

    initial = [1, 17, 0, 10, 18, 11, 6]
    print("Part 1: {}".format(runGame(initial, 2020)))
    print("Part 2 {}".format(runGame(initial, 30000000)))


if __name__ == "__main__":
    main()
