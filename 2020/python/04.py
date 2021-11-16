import re


def getInputDict():
    with open("04.txt") as f:
        lines = "".join(f.readlines()).split("\n\n")
        return list(map(lambda e: {entry.split(":")[0]: entry.split(":")[1].strip() for entry in e.split()}, lines))


hairMatch = re.compile("^#[a-f0-9]{6}$")
passMatch = re.compile("^[0-9]{9}$")
inchesMatch = re.compile("^(59|6[0-9]|7[0-6])in$")
cmMatch = re.compile("^1([5-8][0-9]|9[0-3])cm$")
validEyeColors = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
requiredKeys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def validateOnlyFields(passport):
    return len(list(requiredKeys - set(passport.keys()))) == 0


def validatePassport(passport):
    byr = 1920 <= int(passport["byr"]) <= 2002
    iyr = 2010 <= int(passport["iyr"]) <= 2020
    eyr = 2020 <= int(passport["eyr"]) <= 2030
    hgt = re.match(inchesMatch, passport["hgt"]) != None or re.match(
        cmMatch, passport["hgt"])
    hcl = re.match(hairMatch, passport["hcl"]) != None
    ecl = passport["ecl"] in validEyeColors
    pid = re.match(passMatch, passport["pid"]) != None

    return byr and iyr and eyr and hgt and hcl and ecl and pid


def main():
    inputs = getInputDict()
    print("Part 1: {}".format(
        len(list(filter(lambda i:  validateOnlyFields(i), inputs)))))
    print("Part 2: {}".format(len(list(filter(lambda i:  validatePassport(
        i), filter(lambda p: validateOnlyFields(p), inputs))))))


if __name__ == "__main__":
    main()
