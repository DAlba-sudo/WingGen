from GA.classes.simulation import Simulation
from PlaneGen import PlaneGen
from WingVis import WingVis

if __name__=="__main__":
    sim = Simulation()

    wing = PlaneGen.createWing()
    wingFit = sim.calcFitness(wing)

    print("====== CREATING WING ======")
    PlaneGen.printWing(wing)
    print(f"{wingFit}")

    # sim.loop()
