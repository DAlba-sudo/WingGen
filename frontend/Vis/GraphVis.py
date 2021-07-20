# Important Imports
from frontend.VisUtil.VisModule import VisModule
import tkinter

RANKINGS = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
GRAPH_MARGIN_SIZE = 500
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 20
LINE_WIDTH = 20
MAX_RANK = 1000


class GraphVis(VisModule):
    def __init__(self) -> None:
        VisModule.__init__(self)
    
    def external(self):
        # basic vars
        width = 1000
        height = 500

        # gets the fitness matrix
        fitness_matrix = self.getInfo("fmatrix")
        
        # sets the canvas
        canvas = self.drawCanvas(width, height)
        self.draw_graph(canvas, width, height, fitness_matrix)
        self.draw_ranks(canvas, width, height, fitness_matrix)
        canvas.pack(fill=tkinter.BOTH, expand=True)

        self.top.mainloop()

    def draw_graph(self, canvas, width, height, fitness_matrix):
        canvas.create_line(30, height, width, height)
        canvas.create_line(30, 30, 30, height)
        canvas.create_line(width, 30, width, height)
        ranky_spanky = (height - 30) / 100
        move_x = (width - 30) / len(fitness_matrix)
        move_x2 = 30
        for i in range(len(RANKINGS)):
            canvas.create_text(10, height - (ranky_spanky * RANKINGS[i]), anchor=tkinter.NW, text=RANKINGS[i])
            canvas.create_line(30, height - (ranky_spanky * RANKINGS[i]), width, height - (ranky_spanky * RANKINGS[i]))
        for j in range(len(fitness_matrix)):
            x_move = move_x2
            canvas.create_text(x_move, height, anchor=tkinter.NW, text=f"Gen {j+1}")
            move_x2 += move_x
        return canvas

    def draw_ranks(self, canvas, width, height, fitness_matrix):
        rank_spacing = (height - 30) / 100
        move_by = (width - 30) / len(fitness_matrix)
        x = move_by + 30
        for i in range(len(fitness_matrix)):
            if i != 0:
                x_move = x - move_by
                x_move2 = x
                x += move_by
                rank_y = height - (rank_spacing * fitness_matrix[i - 1])
                rank_y2 = height - (rank_spacing * fitness_matrix[i])
                canvas.create_line(x_move, rank_y, x_move2, rank_y2, fill="blue", width=3)
        return canvas
