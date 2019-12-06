

def getNodeValue(inputs):

    nbrChildren = inputs[0]
    nbrMeta = inputs[1]
    childVals = []

    inputs = inputs[2:]
    if nbrChildren == 0:
        retSum = sum(inputs[:nbrMeta])
        inputs = inputs[nbrMeta:]
        return retSum, inputs
    else:

        for c in range(nbrChildren):
            retVal, inputs = getNodeValue(inputs)
            childVals.append(retVal)
        retSum = 0
        for m in range(nbrMeta):

            if inputs[m]-1 < len(childVals):
                retSum += childVals[inputs[m]-1]
        return retSum, inputs[nbrMeta:]




def part2(inputs):
    retVal, _ = getNodeValue(inputs)
    return retVal




def main():
    inputs = open("../data/input08.txt").readline()
    inputs = list(map(int,inputs.strip().split(" ")))

    print("Part 2: {}".format(part2(inputs)))

main()