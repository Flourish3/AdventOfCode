

def getInput():
    return {(idx, idy, 0): x for idy, y in enumerate(open("17.txt").readlines()) for idx, x in enumerate(y.strip())}


def getActive(conMap, x, y, z):
    dx, dy, dz = [-1, 0, 1], [-1, 0, 1], [-1, 0, 1]
    return len([1 for xs in dx for ys in dy for zs in dz if (x + xs, y + ys, z + zs) != (x, y, z) and (x + xs, y + ys, z + zs) in conMap and conMap[(x + xs, y + ys, z + zs)] == "#"])


def runIter(conMap):
    newMap = conMap.copy()
    for x in range(-20, 20):
        for y in range(-20, 20):
            for z in range(-20, 20):

                around = getActive(conMap, x, y, z)
                if (x, y, z) in conMap and conMap[(x, y, z)] == "#":
                    if (around == 2 or around == 3):
                        newMap[(x, y, z)] = "#"
                    else:
                        newMap[(x, y, z)] = "."
                elif (x, y, z) in conMap and conMap[(x, y, z)] == ".":
                    if around == 3:
                        newMap[(x, y, z)] = "#"
                    else:
                        newMap[(x, y, z)] = "."
                else:
                    newMap[(x, y, z)] = "."

    return newMap


def main():
    conMap = getInput()
    print(conMap)
    for _ in range(1):
        conMap = runIter(conMap)
    print(conMap)
    print(len([v for v in conMap.values() if v == "#"]))


if __name__ == "__main__":
    main()
