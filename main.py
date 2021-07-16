from PlaneGen import PlaneGen
from WingVis import WingVis

if __name__=="__main__":
    wing = PlaneGen.createWing()
    WingVis().visualize(wing)
    