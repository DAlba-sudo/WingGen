from PlaneGen import PlaneGen
from debug import Debug
from GA.classes.simulation import Simulation
from frontend.Vis.WingVis import WingVis

db = Debug()
vis = WingVis()
wing = PlaneGen.createWing()
vis.visualize(wing, [])