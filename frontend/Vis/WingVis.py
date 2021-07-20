# Important Imports
from frontend.VisUtil.VisModule import VisModule

import tkinter as tkinter
from math import floor

class WingVis(VisModule):
    def __init__(self) -> None:
        VisModule.__init__(self)

    def external(self):
        # information gathering stage
        wing = self.getInfo("wing")
        fitness_matrix = self.getInfo("fmatrix")

        # vars
        ROW_NUM = len(wing)
        COL_NUM = len(wing[0])
        width = 1000
        height = 500
        
        # methods to draw the wing
        canvas = self.drawCanvas(width=width, height=height)
        self.draw_squares(canvas, wing, width=width, height=height)
        canvas.pack(fill=tkinter.BOTH, expand=True)
        self.top.mainloop() 

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