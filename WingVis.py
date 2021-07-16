
# Important Imports
from PlaneGen import PlaneGen
import numpy as np
import sys
import random
import datetime

import tkinter as tkinter

class WingVis():
    def __init__(self) -> None:
        pass



    def visualize(self, wing: np.ndarray):
        # basic vars
        ROW_NUM = len(wing)
        COL_NUM = len(wing[0])

        # loads the screen
        root = tkinter.Tk()

        # put labels here

        # starts the loop
        #root.mainloop()
        self.draw_grid_canvas()




    def draw_grid_canvas(self):
        args = sys.argv[1:]

        # Size in squares of world, override from command line
        width = 50
        height = 50
        if len(args) >= 2:
            width = int(args[0])
            height = int(args[1])

        # Size of one square in pixels, override from command line
        global SIDE
        SIDE = 14
        if len(args) == 3:
            SIDE = int(args[2])

        top = tkinter.Tk()

        grid = [[None] * width for _ in range(height)]


        tkinter.mainloop()