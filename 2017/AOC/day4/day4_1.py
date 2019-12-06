inFile = open("input.txt")

valid = 0

for l in inFile.readlines():
    passPhrase = l.split(" ")
    passPhrase[-1] = passPhrase[-1].rsplit("\n")[0]

    errorFlag = False
    for i in range(0, len(passPhrase)  - 1):
        for j in range(i+1, len(passPhrase)):
            if passPhrase[i] == passPhrase[j]:
                errorFlag = True
    if not errorFlag:
        valid += 1

print(valid)