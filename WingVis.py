# Important Imports
from PlaneGen import PlaneGen
import numpy as np
from debug import Debug as db

import tkinter as tkinter
from math import floor


class WingVis():
    def __init__(self) -> None:
        pass

    def visualize(self, wing: np.ndarray):
        # basic vars
        ROW_NUM = len(wing)
        COL_NUM = len(wing[0])
        # PlaneGen.db.printWing(wing)
        db.print(wing)

        # loads the screen
        # root = tkinter.Tk()

        # put labels here

        # starts the loop
        # root.mainloop()
        self.draw_grid_canvas(wing, ROW_NUM, COL_NUM)

    def draw_grid_canvas(self, wing, ROW_NUM, COL_NUM):

        top = tkinter.Tk()
        width = 1000
        height = 700
        top.minsize(width, height)
        canvas = tkinter.Canvas(top, bg="white", height=1000, width=700)
        canvas = self.draw_squares(canvas, wing, width, height)
        canvas.pack()
        canvas.mainloop()

    def draw_squares(self, canvas, wing, width, height):
        x_max = 0
        y_max = 0

        for c in range(len(wing[0])):
            counter = 0
            for r in range(len(wing)):
                if wing[r][c] == 1:
                    counter += 1
            
            if counter > 0:
                y_max += 1

            x_max = max(counter, x_max)

        zoom_w = width / x_max
        zoom_h = height / y_max

        zoom = floor(min(zoom_h, zoom_w))

        for r in range(len(wing)):
            for c in range(len(wing[r])):
                if wing[r][c] == 1:
                    canvas.create_rectangle(c*zoom, r*zoom, zoom * c + zoom, zoom * r + zoom, fill="black", outline='red')

        canvas.update()
        return canvas