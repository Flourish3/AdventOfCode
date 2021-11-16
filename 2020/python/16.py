import re
from functools import reduce

rulePattern = re.compile("^(.+): (\d+)-(\d+) or (\d+)-(\d+)$")


def getInput():
    with open("16.txt") as f:
        rules, ticket, otherTickets = f.read().split("\n\n")
        ruleDict = {}
        for r in rules.split("\n"):
            g = re.match(rulePattern, r).groups()
            ruleDict[g[0]] = set(range(int(g[1]), int(g[2])+1)
                                 ) | set(range(int(g[3]), int(g[4])+1))

    return ruleDict, ticket, otherTickets.split("\n")


def main():
    rules, ticket, tickets = getInput()
    nearbyTickets = list(
        map(lambda x: list(map(lambda x: int(x), x.split(","))), tickets[1:]))
    allowedNums = [y for ys in rules.values() for y in ys]

    print("Part 1: {}".format(
        sum([y for ys in nearbyTickets for y in ys if y not in allowedNums])))

    validTickets = list(filter(lambda y: all(
        map(lambda x: x in allowedNums, y)), nearbyTickets))

    # Figure out which columns can be what key(type etc)
    found = {}
    for key in rules.keys():
        for col in range(len(validTickets[0])):
            if all(map(lambda x: x in rules[key], list(map(lambda x: x[col], validTickets)))):
                if col not in found:
                    found[col] = [key]
                else:
                    found[col].append(key)

    # Go over column - values and elimitate the columns that can be only one value
    final = {}
    changed = 1
    while changed > 0:
        changed = 0
        for k, v in found.items():
            if len(v) == 1 and v[0] not in final:
                final[v[0]] = k
                changed += 1
            elif len(set(v) - set(final.keys())) == 1:
                newK = (set(v) - set(final.keys())).pop()
                if newK not in final:
                    final[newK] = k
                    changed += 1

    departureIdx = [v for k, v in final.items() if k.startswith("departure ")]
    ticket = list(map(lambda x: int(x), ticket.split("\n")[1].split(",")))

    print("Part 2: {}".format(
        reduce(lambda a, b: a*b, [ticket[i] for i in departureIdx])))


if __name__ == "__main__":
    main()
