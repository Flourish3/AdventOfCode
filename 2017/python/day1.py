
def inputSequenceSum(numberList):
    sum = 0
    length = len(numberList)
    for i in range(length):
        #skipNumber = length//2
        skipNumber = 1
        nextIndex = (i+skipNumber) % length
        if numberList[i] == numberList[nextIndex]:
            sum += numberList[i]
    return sum

if __name__ == "__main__":
    with open("input.txt") as f:
        inputString = f.readline().rsplit('\n')[0]
    #puzzleInput = [int(x) for x in list(inputString)]
    puzzleInput = list(map(int, list(inputString)))

    ex1 = [1,1,2,2]
    ex2 = [1,1,1,1]
    ex3 = [9,1,2,1,2,1,2,9]

    sum = inputSequenceSum(puzzleInput)

    print("Puzzle output: {}".format(sum))