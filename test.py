from PlaneGen import PlaneGen
from WingVis import WingVis
from debug import Debug

db = Debug()
vis = WingVis()
wing = PlaneGen.createWing()

print(f"===== GENERATED WING =====")
PlaneGen.printWing(wing)
print("")

print(f"x = {len(wing)}")
print(f"y = {len(wing[0])}")

vis.visualize(wing, [])