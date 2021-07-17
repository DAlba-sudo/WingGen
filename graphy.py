# Important Imports
from tkinter.constants import Y
from PlaneGen import PlaneGen
import numpy as np
from debug import Debug as db
from settings import X_MOD, Y_MOD
from settings import FULL_SCREEN

import tkinter as tkinter
from math import floor

RANKINGS = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
GRAPH_MARGIN_SIZE = 500
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 20
LINE_WIDTH = 20
MAX_RANK = 1000


class GraphVis():
    def __init__(self) -> None:
        self.top = tkinter.Tk()

    def visualize(self, wing: np.ndarray, fitness_matrix: list):
        # basic vars
        ROW_NUM = len(wing)
        COL_NUM = len(wing[0])
        self.draw_grid_canvas(wing, ROW_NUM, COL_NUM, fitness_matrix)

    def draw_grid_canvas(self, wing, ROW_NUM, COL_NUM, fitness_matrix):
        if FULL_SCREEN:
            self.top.attributes('-fullscreen', True)
        width = 1000
        height = 500
        self.top.minsize(width, height)
        canvas = tkinter.Canvas(self.top, bg="white", width=width, height=height)
        canvas = self.draw_graph(canvas, width, fitness_matrix, height)
        canvas = self.draw_ranks(canvas, width, height, fitness_matrix)
        if FULL_SCREEN:
            canvas.pack(fill=tkinter.BOTH, expand=True)
        else:
            canvas.pack()
        self.top.bind('<Escape>', self.toggle_fs)
        self.top.mainloop()

    def toggle_fs(self, dummy=None):
        if FULL_SCREEN:
            state = False if self.top.attributes('-fullscreen') else True
            self.top.attributes('-fullscreen', state)
            if not state:
                self.top.geometry('300x300+100+100')
        else:
            self.top.geometry('300x300+100+100')

    def draw_graph(self, canvas, width, fitness_matrix, height):
        canvas.create_line(30, height, width, height)
        canvas.create_line(30, 30, 30, height)
        canvas.create_line(width, 30, width, height)
        ranky_spanky = (height - 30) / 100
        for i in range(len(RANKINGS)):
            canvas.create_text(10, height - (ranky_spanky * RANKINGS[i]), anchor=tkinter.NW, text=RANKINGS[i])
            canvas.create_line(30, height - (ranky_spanky * RANKINGS[i]), width, height - (ranky_spanky * RANKINGS[i]))
        return canvas

    def draw_ranks(self, canvas, width, height, fitness_matrix):
        fitness_matrix = [10,20,30,40,50,60,50,40,70,90, 30, 75, 19, 36, 100, 2, 11, 51, 67, 45]
        rank_spacing = (height - 30) / 100
        db.print("HOW HOW HOW ! " + str(rank_spacing))
        move_by = (width - 30) / len(fitness_matrix)
        x = move_by + 30
        for i in range(len(fitness_matrix)):
            if i != 0:
                x_move = x - move_by
                x_move2 = x
                x += move_by
                rank_y = height - (rank_spacing * fitness_matrix[i - 1])
                rank_y2 = height - (rank_spacing * fitness_matrix[i])
                canvas.create_line(x_move, rank_y, x_move2, rank_y2, fill="blue")
        return canvas
