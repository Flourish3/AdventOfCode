#Advent of Code - Day 04
from itertools import cycle, accumulate
from collections import Counter
import re

lines = [l.strip() for l in open("../data/input04.txt").readlines()]
checksum_regex = re.compile('(?<=\[)(.*?)(?=\])')
lettersUntilId = re.compile('^.+?(?=\d)')

def part1(lines):
    sectorIdSum = 0
    for l in lines:
        letters = re.search(lettersUntilId,l.replace("-","")).group(0)
        sectorId = re.search('\d+',l).group(0)
        passedChecksum = re.search(checksum_regex,l).group(1)

        c = Counter(list(letters))

        sortedCounter = sorted(c.items(), key=lambda x: (-x[1], x[0]))
        checkSum = "".join(map(lambda x: x[0], sortedCounter[:5]))

        if checkSum == passedChecksum:
            sectorIdSum += int(sectorId)
    return sectorIdSum

def cycleLetter(char, shift):
    return chr((ord(char) - 97 + shift) % 26 + 97)

def part2(lines):
    for l in lines:
        letters = list(re.search(lettersUntilId,l).group(0))
        sectorId = re.search('\d+',l).group(0)     
        decrypted = []
        for c in letters:
            if c == "-":
                decrypted.append(" ")
            else:
                decrypted.append(cycleLetter(c, int(sectorId)))
        decryptedString = "".join(decrypted)

        if "north" in decryptedString.lower():
            print(decryptedString, sectorId)


print(part1(lines))
#print(part2(["qzmt-zixmtkozy-ivhz-343"]))
print(part2(lines))
