from numpy.lib.index_tricks import nd_grid
from debug import Debug
from tkinter.constants import X
from typing import Tuple
import numpy as np
import random
from settings import MINIMUM_BLOCKS_IN_WING, Y_MAX, X_MAX, SPAWN_RATE_BLOCK


class PlaneGen():
    # parameters for wing creation
    X_MAX = X_MAX
    Y_MAX = Y_MAX 
    SPAWN_RATE_BLOCK = SPAWN_RATE_BLOCK

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

    def hasNeighbor(wing: np.ndarray, r, c):

        hasTop = False                  # bool stores whether neighbor is on top
        hasBot = False                  # bool stores whether neighbor is on bot
        hasRight = False                # bool stores whether neighbor is on right
        hasLeft = False                 # bool stores whether neighbor is on left
        
        # validating that block has neighbors
        if r+1 < len(wing):                         # if within bottom bound
            hasBot = (wing[r+1][c] == 1)
        if r-1 >= 0:                 # if within top bound
            hasTop = (wing[r-1][c] == 1)
        if c-1 >= 0: # if within left bound
            hasLeft = (wing[r][c-1] == 1)     
                                                    # if within right bound
        if c+1 < len(wing[0]):
            hasRight = (wing[r][c+1] == 1)

        return hasTop or hasBot or hasRight or hasLeft

    # generates a random wing represented as a one-dimensional 
    # binary number
    def generate(rows:int, cols:int):
        return random.randrange(0, 2**(rows*cols))

    # generates a matrix from the binary number (provides compatability with matrix operations)
    def converFromNum(num:int, rows:int, cols:int) -> Tuple[np.ndarray, int]:
        # vars
        wing: np.ndarray = np.zeros((rows, cols), dtype=int)
        binaryWing:str = bin(num)[2:]        # creates the binary string
        binaryWing = "".rjust(rows*cols - len(binaryWing), "0") + binaryWing

        Debug.print(num)
        Debug.print(binaryWing)
        Debug.print(f"binary len -> {len(binaryWing)}")

        # fills the wing
        for i in range(rows*cols-1):
            if binaryWing[i] == "1":
                r = int((i/cols))
                c = int(i - r*cols)

                Debug.print(f"1 found in index {i} or ({c}, {r})")

                wing[r][c] = 1
        
        return PlaneGen.__filterWing(wing)
    
    # crops the wing matrix
    def __filterWing(wing: np.ndarray) -> Tuple[np.ndarray, int]:
        # vars
        placed = 0
        newWing = np.zeros((len(wing), len(wing[0])))

        # checks how many valid blocks are there and removes
        # blocks without neighbors.
        for r in range(len(wing)):
            for c in range(len(wing[0])):
                if PlaneGen.hasNeighbor(wing, r, c) and wing[r][c] == 1:
                    placed += 1
                    newWing[r][c] = 1
                else:
                    newWing[r][c] = 0

        return newWing, placed

    # provides compatibility with 1D binary string operations
    def toNumber(wing: np.ndarray):
        # vars
        wingOneD = PlaneGen.__convert(wing)
        num = 0 # number representation of the wing
        last_index = len(wingOneD)-1 # represents the index at the tail of the array

        # scan from behind and convert from binary
        for i in range(len(wingOneD)):
            if wingOneD[last_index-i] == 1:
                num += 2**i
        
        return num

    # util method for printing wings
    def printWing(wing: np.ndarray):
        Debug.print(wing)
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
        wing_num = PlaneGen.generate(X_MAX, Y_MAX)
        wing, placed = PlaneGen.converFromNum(wing_num, rows=Y_MAX, cols=X_MAX)

        while not placed >= MINIMUM_BLOCKS_IN_WING:
            wing_num = PlaneGen.generate(X_MAX, Y_MAX)
            wing, placed = PlaneGen.converFromNum(wing_num, rows=Y_MAX, cols=X_MAX)        # filter wing to reduce size
        return wing
        
        