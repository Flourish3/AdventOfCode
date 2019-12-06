inFile = open("input.txt")

inList = list(inFile.readlines())
for l in range(0,len(inList)):
    inList[l] = int(inList[l].rsplit('\n')[0])

steps = 0
index = 0

while index < len(inList) and index >= 0:
    prevIndex = index
    jump = inList[index]
    index += jump
    
    if jump >= 3:
        inList[prevIndex] -= 1
    else:
        inList[prevIndex] += 1
    
    steps += 1

print(steps) 