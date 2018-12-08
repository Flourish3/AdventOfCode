#Advent of Code - Day 05

with open("../data/input05.txt") as f:
    string = f.readline().strip()

def react(input):
    reacted = ""
    for c in input:
        if len(reacted) == 0:
            reacted = c
        elif reacts(c, reacted[-1]):
            reacted = reacted[:-1]
        else:
            reacted += c

    return list(reacted)

def reacts(a, b):
    if abs(ord(a)-ord(b)) == ord('a')-ord('A'):
        return True
    return False

string = list(string)

minLen = len(string)
for i in range(ord('z')-ord('a') + 1):
    c = list(string)

    c = list(filter(lambda a: (ord(a) != ord('A') + i and ord(a) != ord('a') + i), c))

    elim = 1
    while elim > 0:
        before = len(c)
        c = react(c)
        after = len(c)

        elim = before - after
    if len(c) < minLen:
        minLen = len(c)


elim = 1
while elim > 0:
    before = len(string)
    string = react(string)
    after = len(string)

    elim = before - after

print("Part 1: {}".format(len(string)))
print("Part 2: {}".format(minLen))