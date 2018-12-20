# Advent of code - Day 20

def scout(x,y,karta,line):
    nextD = line[0]
    while nextD != "(" and nextD != "$":
        if nextD != "^":
            if nextD == "N":
                karta[(x,y+1)] = "-"
                karta[(x,y+2)] = "."
                y = y+2
            elif nextD == "E":
                karta[(x+1,y)] = "|"
                karta[(x+2,y)] = "."
                x = x+2
            elif nextD == "S":
                karta[(x,y-1)] = "-"
                karta[(x,y-2)] = "."
                y = y-2
            elif nextD == "W":
                karta[(x-1,y)] = "|"
                karta[(x-2,y)] = "."
                x = x-2
            line = line[1:]
            nextD = line[0]





def main():
    # Read input
    line = open("../data/input20.txt").readline().strip()

    # Turn input into rooms
    karta = {}
    x = 0
    y = 0
    karta[(x,y)] = "."
    karta = scout(x,y,karta,line)

main()