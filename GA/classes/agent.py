
import numpy
from PlaneGen import PlaneGen

# individual wing
class Agent():
    def __init__(self) -> None:
        self.genes = PlaneGen.createWing()
        self.fitness = 0
        self.relFit = 0

    # get the fitness
    def getFitness(self) -> float:
        return self.fitness

    # set the fitness
    def setFitness(self, fitness):
        self.fitness = fitness

    # get the relFitness
    def getRelFit(self, fit):
        return self.relFit

    # set the relative fitness
    def setRelFit(self, fit):
        self.relFit = fit

    # get the genes
    def getGenes(self) -> numpy.ndarray:
        return self.genes



