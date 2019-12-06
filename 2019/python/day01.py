lines = [l.strip() for l in open("../data/input01.txt").readlines()]
  
def fuelCalc(mass):
    return mass // 3 - 2

def fuelCalcs(mass):
    while (mass := fuelCalc(mass)) > 0:
        yield mass

def calculateRecursiveFuel(lines):
     return sum([fuel for l in lines for fuel in fuelCalcs(int(l))])

def calculateTotalMass(lines):
    return sum([fuelCalc(int(l)) for l in lines])

print("Part 1: {}".format(calculateTotalMass(lines)))
print("Part 2: {}".format(calculateRecursiveFuel(lines)))
