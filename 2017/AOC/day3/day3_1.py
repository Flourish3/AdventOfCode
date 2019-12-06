#17  16  15  14  13
#18   5   4   3  12
#19   6   1   2  11
#20   7   8   9  10
#21  22  23--->

inPos = 368078

r = 1
while (r*2 -1)**2 < inPos:
    r += 1

smallVal = ((r-1)*2 -1)**2 + 1
bigVal   = (r*2 - 1)**2

NECorner = smallVal - 1 + (r*2 - 1 - 1)

NWCorner = NECorner + (r*2 - 1 - 1)

SWCorner = NWCorner + (r*2 - 1 - 1)

SECorner = SWCorner + (r*2 - 1 - 1)

steps = (bigVal - inPos) 

print(SECorner)

print(steps)

