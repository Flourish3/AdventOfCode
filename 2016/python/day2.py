instructions = []

with open("day2.txt") as f:
    instructions = f.read().strip().split()

number = 5
code = ""

for line in instructions:
    for c in line:
        if   c == 'U' and number > 3:      number -= 3
        elif c == 'D' and number < 7:      number += 3
        elif c == 'L' and number % 3 != 1: number -= 1
        elif c == 'R' and number % 3 != 0: number += 1
    code += str(number)

print(code)

'''
    0
  1 2 3
4 5 6 7 8
  9 A B
    C
'''


stateMap = {'U':0, 'D':1, 'L':2,'R':3}
states = [
    [0,2,0,0],
    [1,5,1,2],
    [0,6,1,3],
    [3,7,2,3],
    [4,4,4,5],
    [1,9,4,6],
    [2,10,5,7],
    [3,11,6,8],
    [8,8,7,8],
    [5,9,9,10],
    [6,12,9,11],
    [7,11,10,11],
    [10,12,12,12]
]

state = 4
actcode = []

for line in instructions:
    for c in line:
        state = states[state][stateMap[c]]
    actcode.append(state+1)
print(''.join(map(lambda v: format(v,'x'), actcode)))
