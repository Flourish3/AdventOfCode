inFile = open("input.txt")

crc = 0

for l in inFile.readlines():
    inList = l.split('\t')
    inList[-1] = inList[-1].rsplit('\n')[0]
    inList = [ int(x) for x in inList]
    crc += max(inList) - min(inList)

print(crc)