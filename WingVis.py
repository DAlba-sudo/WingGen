# Important Imports
from PlaneGen import PlaneGen
import numpy as np
from debug import Debug as db

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
        pass

    def visualize(self, wing: np.ndarray, fitness_matrix: list):
        # basic vars
        ROW_NUM = len(wing)
        COL_NUM = len(wing[0])
        self.draw_grid_canvas(wing, ROW_NUM, COL_NUM, fitness_matrix)

    def draw_grid_canvas(self, wing, ROW_NUM, COL_NUM, fitness_matrix):
        top = tkinter.Tk()
        width = 1500
        height = 700
        top.minsize(width, height)
        canvas = tkinter.Canvas(top, bg="white", width=width, height=height)
        canvas1 = tkinter.Canvas(top, bg="white", width=width, height=height)
        canvas = self.draw_squares(canvas, wing, width, height)
        canvas1 = self.draw_ranks(canvas1, width, height, fitness_matrix)
        canvas.pack()
        canvas1.pack()
        canvas1.mainloop()
        canvas.mainloop()

    def draw_squares(self, canvas, wing, width, height):
        width = width-500
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
        for i in range(len(count)):
            if x_max < count[i]:
                x_max = count[i]
        zoom_w = width / x_max
        zoom_h = height / len(count)
        zoom = zoom_w
        if zoom > zoom_h:
            zoom = zoom_h
        zoom = floor(zoom)

        for i in range(len(wing)):
            for j in range(len(wing[i])):
                if wing[i][j] == 1:
                    canvas.create_rectangle(x, y, x + zoom, y + zoom, fill="red")
                x = x + zoom
            x = 0
            y = y + zoom
        canvas.update()
        return canvas

    def draw_graph(self, canvas, width, fitness_matrix, height):
        print(width)
        print(height)
        print('hi')
        canvas.create_line(width-500, height - 200, width - 100, height)
        canvas.create_line(width-600, height - 300, width - 100, \
                           height - 300)
        for i in range(len(RANKINGS)):
            canvas.create_text(width-600, height - (500+(20 * i)), anchor=tkinter.NW, text=RANKINGS[i])
            x = self.get_x_coordinate(width, i)
            canvas.create_line(x, height - 600, x, height - 300)
            canvas.create_text(x, height - 300, anchor=tkinter.NW, text=RANKINGS[i])
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
        self.draw_graph(canvas, width, fitness_matrix, height)
        print('hello')
        width = canvas.winfo_width()-500
        height = canvas.winfo_height()
        canvas_height = height - (2 * GRAPH_MARGIN_SIZE)
        canvas_width = width - (2 * GRAPH_MARGIN_SIZE)
        rank_spacing = canvas_height / MAX_RANK
        move_by = float(canvas_width / len(RANKINGS))
        """Runs through once for every name the user types in"""
        for i in range(len(fitness_matrix)):
            x_coordinate1 = float((move_by * (i - 1)) + GRAPH_MARGIN_SIZE)
            x_coordinate2 = float((move_by * i) + GRAPH_MARGIN_SIZE)
            rank_y = (rank_spacing * fitness_matrix[i] + GRAPH_MARGIN_SIZE)
            rank_y2 = (rank_spacing * fitness_matrix[i] + GRAPH_MARGIN_SIZE)
            canvas.create_text((x_coordinate1 + TEXT_DX), rank_y, anchor=tkinter.SW, \
                                   text=f'Fitness: {fitness_matrix[i]}', fill="red")
            canvas.create_line(x_coordinate1, rank_y, x_coordinate2, rank_y2, fill="blue",
                                   width=LINE_WIDTH)
            canvas.create_text((x_coordinate2 + TEXT_DX), rank_y2, anchor=tkinter.SW, \
                                   text=f'Fitness: {fitness_matrix[i]}', fill='green')






        return canvas