# Advent of code - Day 23

# Advent of code - Day 17

from intcode import *
import threading
import time

inp = [int(ins) for ins in open("../data/input23.txt").read().split(",")]

class Message():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Computer():
    def __init__(self, address, inputData):
        self.address = address
        self.machine = Machine([j for j in inputData])
        self.inQueue = []
        try:
            print(self.address)
            self.machine.run_machine([self.address, -1])
        except Output as e:
            print(e.output)
            address = e.output
            outputMode = 1
            pass 
    
    def addToQueue(self, msg):
        self.inQueue.append(msg)
    
    def runMachine(self):
        pass

class programThread (threading.Thread):
    def __init__(self, address):
        threading.Thread.__init__(self)
        self.machine = Machine([j for j in inp])
        self.address = address
        

    def run(self):
        outputMode = 0
        address = 0
        x,y = 0,0
        try:
            machine.run_machine([self.address])
        except Output as e:
            address = e.output
            outputMode = 1
            pass 
            
        while True:
            try:
                machine.run_machine([self.address])
            except Output as e:
                if outputMode == 0:
                    address = e.output
                    outputMode = 1
                    pass
                elif outputMode == 1:
                    x = e.output
                    outputMode = 2
                    pass
                else:
                    y = e.output

                    # Get lock to synchronize threads
                    threadLock.acquire()
                    print_time(self.name, self.counter, 3)
                    # Free lock to release next thread
                    threadLock.release()
                    outputMode = 0
            except Interrupt:
                break 


def part1():
    computers = [Computer(address, inp) for address in range(50)]

    grid = {}
    output_type = 0

print("Part 1: {}".format(part1()))

#print("Part 2: {}".format(part2()))