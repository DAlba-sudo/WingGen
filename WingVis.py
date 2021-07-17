# Important Imports
from tkinter.constants import Y
from PlaneGen import PlaneGen
import numpy as np
from debug import Debug as db
from settings import X_MOD, Y_MOD

import tkinter as tkinter
from math import floor

RANKINGS = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
GRAPH_MARGIN_SIZE = 500
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 20
LINE_WIDTH = 20
MAX_RANK = 1000

class WingVis():
    def __init__(self) -> None:
        self.top = tkinter.Tk()

    def visualize(self, wing: np.ndarray, fitness_matrix: list):
        # basic vars
        ROW_NUM = len(wing)
        COL_NUM = len(wing[0])
        self.draw_grid_canvas(wing, ROW_NUM, COL_NUM, fitness_matrix)

    def draw_grid_canvas(self, wing, ROW_NUM, COL_NUM, fitness_matrix):
        self.top.attributes('-fullscreen', True)
        width = 1000
        height = 500
        self.top.minsize(width, height)
        canvas = tkinter.Canvas(self.top, bg="white", width=width, height=height)
        canvas = self.draw_squares(canvas, wing, width, height)
        canvas.pack(fill=tkinter.BOTH, expand=True)
        self.top.bind('<Escape>', self.toggle_fs)
        self.top.mainloop()

    def toggle_fs(self, dummy=None):
        state = False if self.top.attributes('-fullscreen') else True
        self.top.attributes('-fullscreen', state)
        if not state:
            self.top.geometry('300x300+100+100')


    def draw_squares(self, canvas, wing, width, height):
        width = width
        height = height
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