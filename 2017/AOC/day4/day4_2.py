inFile = open("input.txt")

def isAnagram(s1, s2):
    if ''.join(sorted(s1)) == ''.join(sorted(s2)):
        return True
    return False


valid = 0

for l in inFile.readlines():
    passPhrase = l.split(" ")
    passPhrase[-1] = passPhrase[-1].rsplit("\n")[0]
    print(''.join(sorted(passPhrase[0])))

    errorFlag = False
    for i in range(0, len(passPhrase)  - 1):
        for j in range(i+1, len(passPhrase)):
            if isAnagram(passPhrase[i],  passPhrase[j]):
                errorFlag = True
    if not errorFlag:
        valid += 1

print(valid)