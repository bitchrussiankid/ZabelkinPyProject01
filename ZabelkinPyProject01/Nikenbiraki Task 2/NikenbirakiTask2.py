import random
import itertools
import time

def fillingBox(N):
    box = [[0 for i in range(N)] for j in range(N)] # create the empty NxN box

    boxWeight = 0                                   # total box weight
    filledCells = 0                                 # number of filled cells

    maxCells = N * N * 0.7            # the maximum number of cells that can be filled
    maxWeight = N * N * 0.7 * 5.5     # the maximum weight that can be achieved


    for i in itertools.count():
        jarWeight = random.randint(0, 10)
        indexX = random.randint(0, N - 1)
        indexY = random.randint(0, N - 1)
    
        # total box weight and filled cells:
        if box[indexX][indexY] == 0:
            boxWeight += jarWeight
            if jarWeight != 0:
                filledCells += 1
        else: 
            boxWeight = boxWeight - box[indexX][indexY] + jarWeight
            if jarWeight == 0:
                filledCells -= 1
    
        # we put the jar in the cell:
        box[indexX][indexY] = jarWeight

        # check the conditions:
        if boxWeight > maxWeight or filledCells > maxCells:
            break
        
    print(box)
    print(boxWeight)
    print(filledCells)

N = 3
fillingBox(N)