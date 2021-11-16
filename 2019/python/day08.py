line = open("../data/input08.txt").readline().strip()

width = 25
height = 6

lineList = list(map(int, list(line)))
index = 0
ans = []
image = []
while (index+1)*width*height <= len(lineList):
    current = lineList[index*width*height:(index+1)*width*height]
    ans.append((current.count(0), current.count(1)*current.count(2)))
    image.append(current)
    index += 1

completeImage = []
for pixel in range(width*height):
    for layer in range(len(image)):
        currentColor = image[layer][pixel]
        if  currentColor != 2:
            completeImage.append(currentColor)
            color = currentColor
            break

print(sorted(ans, key=lambda x: x[0])[0][1]) #Part 1
index = 0
while (index+1)*width <= len(completeImage):
    print("".join(list(map(lambda x: chr(9608) if x == 1 else " ", completeImage[index*width:(index+1)*width])))) # Part 2
    index += 1
