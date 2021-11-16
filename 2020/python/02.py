import re


class PW:
    def __init__(self, min, max, letter, pw):
        self.min = min
        self.max = max
        self.letter = letter
        self.pw = pw


def parseLine(line):
    pat = "^(\d+)-(\d+) (\S): (\S+)$"

    ma = re.match(pat, line).groups()

    return PW(int(ma[0]), int(ma[1]), ma[2], ma[3])


def validatePW(pw):
    count = pw.pw.count(pw.letter)
    return count >= pw.min and count <= pw.max


def validateNew(pw):
    l = list(pw.pw)
    return (l[pw.min - 1] == pw.letter) != (l[pw.max - 1] == pw.letter)


with open("02.txt") as f:
    lines = [parseLine(x) for x in f.readlines()]
    print(len(list(filter(lambda x: validatePW(x), lines))))
    print(len(list(filter(lambda x: validateNew(x), lines))))
