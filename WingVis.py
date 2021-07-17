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
        if not state:
            self.top.attributes('-fullscreen', state)
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

    def draw_graph(self, canvas, width, fitness_matrix, height):
        print(width)
        print(height)
        print('hi')
        x1 = width/2
        y1 = height-(height*.7)
        canvas.create_line(x1, height, width, height)
        canvas.create_line(x1, y1, x1, height)
        canvas.create_line(width, y1, width, height)
        for i in range(len(RANKINGS)):
            canvas.create_text(x1 - 20, height - (35 * i), anchor=tkinter.NW, text=RANKINGS[i])
            x = self.get_x_coordinate(width, i)
            canvas.create_line(x1, height - (35 * i), width, height - (35 * i))
            #x2 += x2/10
            #canvas.create_text(x, height - 300, anchor=tkinter.NW, text=RANKINGS[i])
        return canvas

    def get_x_coordinate(self, width, year_index):
        """
        Given the width of the canvas and the index of the current year
        in the YEARS list, returns the x coordinate of the vertical
        line associated with that year.

        Input:
            width (int): The width of the canvas
            year_index (int): The index of the current year in the YEARS list
        Returns:
            x_coordinate (float): The x coordinate of the vertical line associated
                                  with the specified year.
        """
        move_by = float((width - (2 * GRAPH_MARGIN_SIZE)) / len(RANKINGS))
        x_coordinate = float((move_by * year_index) + GRAPH_MARGIN_SIZE) + 400
        return x_coordinate

    def draw_ranks(self, canvas, width, height, fitness_matrix):
        print('hello')
        width1 = width/2
        height1 = height/2
        rank_spacing = (height - (35 * 10)) / 100
        move_by = floor(width1 / len(fitness_matrix))
        x = move_by + width1
        for i in range(len(fitness_matrix)):
            if i != 0:
                x_move = floor((move_by * i - 1) + width1)
                x_move2 = floor((move_by * i) + width1)
                delta_y = rank_spacing * fitness_matrix[i]
                x_coordinate1 = x - move_by
                x_coordinate2 = x
                x += move_by
                rank_y = (rank_spacing * fitness_matrix[i-1])
                rank_y2 = (rank_spacing * fitness_matrix[i])
                #canvas.create_text((x_coordinate1 + TEXT_DX), rank_y, anchor=tkinter.SW, \
                                     #  text=f'Fitness: {fitness_matrix[i]}', fill="red")
                canvas.create_line(x_move, rank_y, x_move2, rank_y2, fill="blue",
                                       width=LINE_WIDTH)
                #canvas.create_text((x_coordinate2 + TEXT_DX), rank_y2, anchor=tkinter.SW, \
                                     #  text=f'Fitness: {fitness_matrix[i]}', fill='green')

        canvas.update()
        return canvas