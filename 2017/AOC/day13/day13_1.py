with open("input.txt") as f:
    
    security = {}
    layers = 0
    severity = 0

    for line in f:
        inLine = list(map(int, line.strip().split(':')))
        security[inLine[0]] = inLine[1]
        if inLine[0] > layers:
            layers = inLine[0]

    foundDelay = False
    delay = 0
    while not foundDelay:
        severity = 0
        for i in range(0, layers+1):
            if i in security:
                if ((i+delay) % ((security[i]-1)*2)) == 0:
                    severity += i*security[i]
                    if i == 0:
                        severity += 1          
        if severity == 0 or delay > 10000000:
            foundDelay = True
        else:
            delay += 1
    print(delay)