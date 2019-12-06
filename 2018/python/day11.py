#Advent of Code - Day 11


def solve(serialNumber):

    grid = [[0]*300 for i in range(300)]

    for x in range(300):
        for y in range(300):
            rackID = (x+1)+10
            grid[x][y] = (x+1)+10 #rack ID
            grid[x][y] *= (y+1)  #Init power level
            grid[x][y] += serialNumber #increase by serial number
            grid[x][y] *= rackID #Multiply by rack ID
            if grid[x][y] < 100:
                grid[x][y] = 0
            else:
                grid[x][y] = (grid[x][y] // 100) % 10

            grid[x][y] -= 5


    sumMat = [[0]*300 for i in range(300)]

    for x in range(300):
        for y in range(300):
            if x == 0 and y == 0:
                sumMat[x][y] = grid[x][y]
            if x == 0 and y != 0:
                sumMat[x][y] = grid[x][y] + sumMat[x][y-1]
            if x != 0 and y == 0:
                sumMat[x][y] = grid[x][y] + sumMat[x-1][y]
            else:
                sumMat[x][y] = grid[x][y] + sumMat[x][y-1] + sumMat[x-1][y] - sumMat[x-1][y-1]

    maxPower = 0
    maxX = maxY = maxGrid = 0

    for s in range(1,300):
        for x in range(s,300):
            for y in range(s,300):
                summa = sumMat[x][y] - sumMat[x][y-s] - sumMat[x-s][y] + sumMat[x-s][y-s]
                if summa > maxPower:
                    maxPower = summa
                    maxX = x
                    maxY = y
                    maxGrid = s

    return (maxX+1)-(maxGrid-1), (maxY+1)-(maxGrid-1), maxGrid



def main():
    input = 1718
    print("Solution: {}".format(solve(input)))

    input = 18
    print("Test 1: {}".format(solve(input)))

    input = 42
    print("Test 2: {}".format(solve(input)))



main()