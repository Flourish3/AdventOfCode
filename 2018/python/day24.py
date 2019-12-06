# Advent of code - Day 24

import re

class Group():
    def __init__(self, gp, nbr, hp, weak, immune, ap, initiative):
        self.nbr = nbr
        self.hp = hp
        self.weak = weak
        self.immune = immune
        self.ap = ap
        self.initiative = initiative
        self.effective = self.nbr*self.ap
        self.gp = gp

    def attack(self, effective, typ):
        pass

    def __lt__(self, other):
        if self.effective < other.effective:
            return True
        elif self.effective == other.effective and self.initiative < other.initiative:
            return True
        else:
            return False

def main():
    groups = []
    '''
    Immune System:
    2991 units each with 8084 hit points (weak to fire) with an attack that does 19 radiation damage at initiative 11
    4513 units each with 3901 hit points (weak to slashing; immune to bludgeoning, radiation) with an attack that does 7 bludgeoning damage at initiative 12
    5007 units each with 9502 hit points (immune to bludgeoning; weak to fire) with an attack that does 16 fire damage at initiative 2
    2007 units each with 5188 hit points (weak to radiation) with an attack that does 23 cold damage at initiative 9
    1680 units each with 1873 hit points (immune to bludgeoning; weak to radiation) with an attack that does 10 bludgeoning damage at initiative 10
    1344 units each with 9093 hit points (immune to bludgeoning, cold; weak to radiation) with an attack that does 63 cold damage at initiative 16
    498 units each with 2425 hit points (immune to fire, bludgeoning, cold) with an attack that does 44 slashing damage at initiative 3
    1166 units each with 7295 hit points with an attack that does 56 bludgeoning damage at initiative 8
    613 units each with 13254 hit points (immune to radiation, cold, fire) with an attack that does 162 radiation damage at initiative 15
    1431 units each with 2848 hit points (weak to radiation) with an attack that does 19 cold damage at initiative 1
    '''

    '''
    Infection:
    700 units each with 47055 hit points (weak to fire; immune to slashing) with an attack that does 116 fire damage at initiative 14
    2654 units each with 13093 hit points (weak to radiation) with an attack that does 8 radiation damage at initiative 19
    5513 units each with 18026 hit points (immune to radiation; weak to slashing) with an attack that does 6 slashing damage at initiative 20
    89 units each with 48412 hit points (weak to cold) with an attack that does 815 radiation damage at initiative 17
    2995 units each with 51205 hit points (weak to cold) with an attack that does 28 slashing damage at initiative 7
    495 units each with 21912 hit points with an attack that does 82 cold damage at initiative 13
    2911 units each with 13547 hit points with an attack that does 7 slashing damage at initiative 18
    1017 units each with 28427 hit points (immune to fire) with an attack that does 52 fire damage at initiative 4
    2048 units each with 29191 hit points (weak to bludgeoning) with an attack that does 22 bludgeoning damage at initiative 6
    1718 units each with 15725 hit points (immune to cold) with an attack that does 18 slashing damage at initiative 5
    '''
    lines = open("../data/input24.txt").readlines()
    immune = False
    for l in lines:
        if l.strip() == "Immune System:"
            immune = True
        elif l.strip() == "Infection:"
            immune = False
        elif l != "\n":
            g = re.findall(r"(\d+) units each with (\d+) hit points ((weak to fire)) with an attack that does (\d+) (\s+) damage at initiative (\d+)",l)
            print(g)


main()