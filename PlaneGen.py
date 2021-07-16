from tkinter.constants import X
from typing import Tuple
import numpy as np
import random
from settings import MINIMUM_BLOCKS_IN_WING


class PlaneGen():
    # parameters for wing creation
    X_MAX = 60
    Y_MAX = 150 
    SPAWN_RATE_BLOCK = 0.50

    # blank initializer
    def __init__(self) -> None:
        pass

    # creates an empty numpy array (which represents the wing as a matrix)
    def __createEmpty() -> np.ndarray:
        return np.zeros((PlaneGen.X_MAX, PlaneGen.Y_MAX))

    def __convert(wing: np.ndarray) -> list:
        wingOneD = []
        for r in range(len(wing)):
            for c in range(len(wing[0])):
                wingOneD.append(wing[r][c])
        
        return wingOneD

    # randomly fills said array
    def __randomFill() -> Tuple[np.ndarray, int]:
        # vars
        emptyArr = PlaneGen.__createEmpty()     # wing represented as a matrix
        placed = 0                              # keeps track of the number of blocks placed

        # random placement loop
        for r in range(len(emptyArr)):
            for c in range(len(emptyArr[r])):
                hasTop = False                  # bool stores whether neighbor is on top
                hasBot = False                  # bool stores whether neighbor is on bot
                hasRight = False                # bool stores whether neighbor is on right
                hasLeft = False                 # bool stores whether neighbor is on left

                # 'great filer' (i.e., block is spawned if above threshold)
                if random.random() >= PlaneGen.SPAWN_RATE_BLOCK:

                    # places genesis block regardless of neighbors
                    if placed == 0:
                        emptyArr[r][c] = 1
                        placed += 1

                    
                    # validating that block has neighbors
                    if r+1 < len(emptyArr):                     # if within bottom bound
                        hasBot = emptyArr[r+1][c] == 1
                    if r-1 >= 0 and not hasTop:                 # if within top bound
                        hasTop = emptyArr[r-1][c] == 1
                    if c-1 >= 0 and (not hasTop or not hasBot): # if within left bound
                        hasLeft = emptyArr[r][c-1] == 1     
                                                                # if within right bound
                    if c+1 < len(emptyArr[0]) and (not hasTop or not hasBot or not hasLeft):
                        hasRight = emptyArr[r][c+1] == 1

                    # if has any neighbors, place
                    if hasTop or hasBot or hasLeft or hasRight: 
                        emptyArr[r][c] = 1
                        placed += 1
        
        return emptyArr, placed
    
    # util method for printing wings
    def printWing(wing: np.ndarray):
        for i in wing:
            if 1 in i:
                print("")
                for j in i:
                    if j == 0:
                        print(" ", end="")
                    else:
                        print(".", end="")
        
        print("")

    # public function for creating wings
    def createWing() -> np.ndarray:
        # init wing with proper num of placed blocks
        wing, placed = PlaneGen.__randomFill()
        while not placed >= MINIMUM_BLOCKS_IN_WING:
            wing, placed = PlaneGen.__randomFill()

        # filter wing to reduce size


        return wing