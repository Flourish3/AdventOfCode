import re
from typing import Dict, List, Tuple


class RuleNode():
    def __init__(self, ruleId: str, first: str, second: str):
        self.ruleId = ruleId
        self.first = first.split(" ")
        if second != None:
            self.second = second.split(" ")
    
    def resolveRule(self, ruleDict):
        firstAlt = []

        secondAlt = []
        total = firstAlt.extend[secondAlt]
        return total


messagePat = re.compile("^[ab]*$")

# 0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"

# [[a]]


def evaluateRules(rules: Dict[str, List[str]]) -> Dict[str, List[str]]:
    changed = 1
    while changed > 0:
        changed = 0
        for k, v in rules.items():
            newL = []
            for alt in v:
                for num in alt.split(" "):
                    if num in rules:
                        if len(newL) == 0:
                            newL.append(rules[num])
                        else:
                            for subList in newL:
                                subList.append()


def getInput() -> Tuple[Dict[str, List[str]], List[str]]:
    rules, messages = {}, []
    for line in open("19.txt").readlines():
        if re.match(messagePat, line) != None:
            messages.append(line.strip())
        else:
            rule = line.strip().split(": ")
            if rule[1] == "\"a\"" or rule[1] == "\"b\"":
                rules[rule[0]] = [list(rule[1])[1]]
            else:
                rules[rule[0]] = rule[1].split(" | ")

    return rules, messages


def applyRule(rule: List[str], message: str) -> bool:
    return message in rule


def main():
    ruleDic, messages = getInput()
   # print("Part 1: {}".format(len(list(filter(lambda x: applyRule(ruleDic["0"], x), messages)))))
    print(ruleDic, messages)


if __name__ == "__main__":
    main()
