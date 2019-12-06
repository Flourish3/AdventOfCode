#Advent of Code - Day 05

import hashlib 

doorId = open("../data/input05.txt").readline().strip()

def hasFiveLeadingZeros(doorHash):
    return set(list(doorHash.hexdigest())[0:5]) == set('0')

def part1(doorId):
    index = 0
    password = []
    while True:
        doorHash = hashlib.md5((doorId + str(index)).encode())
        index += 1
        if len(password) == 8:
            break

        if(hasFiveLeadingZeros(doorHash)):
            print(list(doorHash.hexdigest())[5])
            password.append(list(doorHash.hexdigest())[5])
    return "".join(password)

def part2(doorId):
    index = 0
    password = [-1,-1,-1,-1,-1,-1,-1,-1]
    found = 0
    while True:
        doorHash = hashlib.md5((doorId + str(index)).encode())
        index += 1
        if found == 8:
            break

        if(hasFiveLeadingZeros(doorHash)):
            hashList = list(doorHash.hexdigest())
            if hashList[5].isdigit() and int(hashList[5]) < 8 and password[int(hashList[5])] == -1:
                password[int(hashList[5])] = hashList[6]
                print("".join(map(lambda x: str(x),password)))
                found += 1

    return "".join(map(lambda x: str(x),password))
#print(part1(doorId))
print(part2(doorId))