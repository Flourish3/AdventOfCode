inFile = open("input.txt")

crc = 0

for l in inFile.readlines():
    inList = l.split('\t')
    inList[-1] = inList[-1].rsplit('\n')[0]
    inList = [ int(x) for x in inList]

    for i in range(0, len(inList)):
        for j in range(0,len(inList)):
            if j != i:
                if  inList[j] % inList[i] == 0:
                    crc += inList[j] / inList[i]

print(crc)