from settings import FULL_SCREEN
from debug import Debug as db
from math import floor

import numpy as np
import tkinter as tk


# this is the wrapper class for all visualization modules
# used throughout the project. This will allow for better
# manipulation of our codebase.
class VisModule():
    
    def __init__(self) -> None:
        # vars
        self.top = tk.Tk()
        self.info = {}

        # initializes the visualization module
        self.__initRoot()

    # general method for initializing 'top'
    def __initRoot(self):
        self.top.attributes("-fullscreen", FULL_SCREEN)
        self.top.bind('<Escape>', self.toggle_fs)

    # used for adding information to the exec
    # loop (i.e., if your canvas needs information),
    # you should use this func.
    def addInfo(self, key:str, val):
        self.info[key] = val

    # getters for info
    def getInfo(self, key:str):
        return self.info[key]

    # general func for adding drawing a canvas
    def drawCanvas(self, width: int, height: int) -> tk.Canvas:
        self.top.minsize(width, height)
        canvas = tk.Canvas(self.top, bg="white", width=width, height=height)
        return canvas

    # main loop
    def visualize(self, wing: np.ndarray, fmatrix: list):
        # row and col info
        ROW_NUM = len(wing)
        COL_NUM = len(wing[0])

        # adds the info
        self.addInfo("wing", wing)
        self.addInfo("ROW_NUM", ROW_NUM)
        self.addInfo("COL_NUM", COL_NUM)
        self.addInfo("fmatrix", fmatrix)

        # method to override in external environment
        self.external()
    
    # the method invoked from the 'outside'
    def external(self):
        pritn("Executing the default VisModule 'external'.")

    # misc. methods
    def toggle_fs(self, dummy=None):
        state = False if self.top.attributes('-fullscreen') else True
        if not state:
            self.top.attributes('-fullscreen', state)
            self.top.geometry('300x300+100+100')