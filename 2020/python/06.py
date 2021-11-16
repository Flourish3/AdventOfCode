from functools import reduce

def getInput():
    with open("06.txt") as f:
        return f.read().split("\n\n")

def countOnlyIncluded(group: str) -> int:
    return len(reduce(lambda a,b: a & b, [set(list(g)) for g in group.strip().split("\n")]))
    
def countUnique(group: str) -> int:
    return len(set(list(group.replace("\n", ""))))

def main():
    input = getInput()
    print("Part 1: {}".format(sum(list(map(lambda x: countUnique(x), input)))))
    print("Part 2: {}".format(sum(list(map(lambda x: countOnlyIncluded(x), input)))))

if __name__ == "__main__":
    main()