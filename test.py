from PlaneGen import PlaneGen
from WingVis import WingVis
from debug import Debug
from GA.classes.simulation import Simulation

db = Debug()
vis = WingVis()
wing = PlaneGen.createWing()
sim = Simulation()

print(f"===== GENERATED WING =====")
PlaneGen.printWing(wing)
print(f"{sim.calcFitness(wing)}")

vis.visualize(wing, [])