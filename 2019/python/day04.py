# Advent of code - Day 04

minRange = 168630
maxRange = 718098

def hasDuplicate(number):
    prevNum = 0
    for num in list(str(number)):
        if int(num) == prevNum:
            return True
        else:
            prevNum = int(num)
    return False

def neverDecrese(number):
    prevNum = 0
    for num in list(str(number)):
        if int(num) < prevNum:
            return False
        else:
            prevNum = int(num)
    return True

def hasDuplicateOnlyTwo(number):
    ls = list(str(number))
    resDict = {}
    current = int(ls[0])
    resDict[current] = 1
    
    for num in ls[1:]:
        if int(num) == current:
            resDict[current] += 1
        else:
            resDict[int(num)] = 1
        current = int(num)
    
    counts = [v for k,v in resDict.items()]
    return 2 in counts

def part1(minRange, maxRange):
    count = 0
    for candidate in range(minRange, maxRange + 1):
        if hasDuplicate(candidate) and neverDecrese(candidate):
            count += 1
    
    return count

def part2(minRange, maxRange):
    count = 0
    for candidate in range(minRange, maxRange + 1):
        if hasDuplicateOnlyTwo(candidate) and neverDecrese(candidate):
            count += 1
    
    return count

print("Part1: {}".format(part1(minRange, maxRange)))
print("Part2: {}".format(part2(minRange, maxRange)))
  