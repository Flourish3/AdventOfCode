
def determineLoopSize(sub, pubKey):
    div = 20201227
    key = 1
    loop = 0

    while key != pubKey:
        key = key * sub
        key = key % div
        loop += 1

    return loop


def encLoop(pub, loop):
    key = 1
    div = 20201227

    for i in range(loop):
        key = key * pub
        key = key % div

    return key


def main():
    cardPub = 15113849
    doorPub = 4206373

    cardLoop, doorLoop = determineLoopSize(
        7, cardPub), determineLoopSize(7, doorPub)
    print("Part 1: {}".format(encLoop(cardPub, doorLoop)))


if __name__ == "__main__":
    main()
