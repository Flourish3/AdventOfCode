from math import ceil
from functools import reduce

def mult(M, m):
    gcd, x,y = gcdExtended(M//m, m)
    return (M//m)*x

def main():
    with open("13.txt") as f:
        timestamp = int(f.readline())
        busTimes = f.readline().split(",")
        onlyTime = [int(t) for t in busTimes if t != "x"]
        mini = min(list(map(lambda x: (x, x*ceil(timestamp/x)-timestamp), onlyTime)), key=lambda x: x[1])
        print(mini[0]*mini[1])

        print(",".join(["(t+{})%{}=0".format(idx, v) for idx,v in list(filter(lambda x: x[1] != "x", enumerate(busTimes)))]))
       
        col = [[idx, int(v)] for idx,v in list(filter(lambda x: x[1] != "x", enumerate(busTimes)))]
        print(col)
        M = reduce(lambda a,b: a*b, list(map(lambda x: x[1], col)))
        T = list(map(lambda x: mult(M, x[1]) , col))
        print(M)
        print(T)

        S = sum(map(lambda x: reduce(lambda a,b: a*b, x),zip(T, list(map(lambda x: x[0], col)))))

        print("Part 2: {}".format((M - S) // sum(T)))

def gcdExtended(a, b):  
    # Base Case  
    if a == 0 :   
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)  
     
    # Update x and y using results of recursive  
    # call  
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd,x,y 

if __name__ == "__main__":
    main()