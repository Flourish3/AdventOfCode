with open("day3.txt") as f:
    count = 0
    for line in f:
        sides = list(map(int,line.strip().split()))

        if sides[0]+sides[1]>sides[2] and sides[1]+sides[2]>sides[0] and sides[2]+sides[0]>sides[1]:
            count += 1
    print(count)