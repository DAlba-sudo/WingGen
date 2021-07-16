from PlaneGen import PlaneGen
from WingVis import WingVis

vis = WingVis()
wing = PlaneGen.createWing()

print(f"===== GENERATED WING =====")
PlaneGen.printWing(wing)
print("")

vis.visualize(wing)