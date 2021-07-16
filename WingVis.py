# Important Imports
from PlaneGen import PlaneGen
import numpy as np
import sys
import random
import datetime

import tkinter as tkinter
from math import floor


class WingVis():
    def __init__(self) -> None:
        pass

    def visualize(self, wing: np.ndarray):
        # basic vars
        ROW_NUM = len(wing)
        COL_NUM = len(wing[0])
        # PlaneGen.printWing(wing)
        print(wing)

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
        counter = 0
        count = []

        x = 0
        y = 0

        for i in range(len(wing)):
            for j in range(len(wing[i])):
                counter += 1
            if counter != 0:
                count.append(counter)
            counter = 0
        print(count)
        for i in range(len(count)):
            if x_max < count[i]:
                x_max = count[i]
        print(x_max)
        zoom_w = width / x_max
        print(zoom_w)
        print(len(count))
        zoom_h = height / len(count)
        print(zoom_h)
        zoom = zoom_w
        print(zoom)
        if zoom > zoom_h:
            zoom = zoom_h
        zoom = floor(zoom)
        print(zoom)

        for i in range(len(wing)):
            for j in range(len(wing[i])):
                if wing[i][j] == 1:
                    canvas.create_rectangle(x, y, x + zoom, y + zoom, fill="red")
                x = x + zoom
            x = 0
            y = y + zoom
        canvas.update()
        return canvas