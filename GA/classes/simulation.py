from frontend.Vis.GraphVis import GraphVis
from frontend.Vis.WingVis import WingVis
from debug import Debug
import numpy
from PlaneGen import PlaneGen
from random import choice, random, randrange
from .agent import Agent
from math import floor
from settings import POPULATION_SIZE, DEATH_THRESH

class Simulation():
    DEATH_THRESH = DEATH_THRESH            # percentage of population sent to death row

    def __init__(self, size=POPULATION_SIZE) -> None:
        # params
        self.size = size

        # vars
        self.popPool = []
        self.fitnessMatrix = []

        # init
        self.__populate()           # fills the population

    # populates the pool with random agent
    def __populate(self):
        for i in range((self.size)):
            wing = Agent()
            self.popPool.append(wing)
            
            print("====== CREATING WING ======")
            PlaneGen.printWing(wing.getGenes())
            print("")


    # calc fitness as a func of the wind-facing surface area
    def __calcFitness(self, wing: numpy.ndarray):
        sum = 0
        for c in range(len(wing[0])):
            SA = 0
            for r in range(len(wing)):
                # if the left of the block is a blank, 
                # we assume it would be hit by wind
                try:
                    if wing[r][c-1] == 0 and wing[r][c] == 1:
                        SA += 1
                except IndexError:
                    pass
            # add the surface area
            sum += SA

        return sum

    # public calcfitness
    def calcFitness(self, wing: numpy.ndarray):
        return self.__calcFitness(wing)

    def __assignFitness(self):
        # 'global' vars
        sumFit = 0

        # sets the raw fitness
        for i in range(len(self.popPool)):
            # exctract wing
            wing: numpy.ndarray = self.popPool[i].getGenes()
            print("====== RATING WING ======")
            PlaneGen.printWing(wing)

            # find fitness
            fitness = self.__calcFitness(wing)
            sumFit = max(fitness, sumFit)

            # assign fitness
            self.popPool[i].setFitness(fitness)
        
        # relative fit
        max_relFit = 0

        # makes them relative
        for i in range(len(self.popPool)):
            relFit = (1 / self.popPool[i].getFitness())

            # get the raw fit and make rel
            self.popPool[i].setFitness(relFit)

            max_relFit = max(relFit, max_relFit)

        print(max_relFit)
        self.fitnessMatrix.append(max_relFit * 100)

    # deletes individuals not fit for selection
    def __deathRow(self):
        death_num = floor( self.size * Simulation.DEATH_THRESH );
        while not len(self.popPool) < death_num:
            print("Trying to delete people!")
            found = False

            for i in range(len(self.popPool)):
                if self.popPool[i].getFitness() > random():
                    self.popPool.pop(i)
                    found = True
                    break
            
            if not found:
                self.popPool.pop(randrange(0, len(self.popPool)-1)) 

    # selects two random individuals
    def __select(self) -> list:
        sq_fitness = []
        print("Choosing parents!")
        parents = []
        x = choice(self.popPool)
        y = choice(self.popPool)
        parents.append(x)
        parents.append(y)
        return parents        

    # introduces children to population
    def __reproduce(self):
        parents = self.__select()
        print("In reproduction stage!")

        # parents 
        p1:Agent = parents[0]
        p2:Agent = parents[1]

        # creates child
        child = Agent()
        childWing = numpy.zeros((PlaneGen.X_MAX, PlaneGen.Y_MAX))

        # merges the parent and child 
        for r in range(len(child.getGenes())):
            for c in range(len(child.getGenes()[0])):
                if p1.getGenes()[r][c] == 1 and p2.getGenes()[r][c] == 1:
                    childWing[r][c] = 1

        child.genes = childWing

        # adds child to population
        self.popPool.append(child)
 
    def loop(self):
        for i in range(int(input("Number of generations: "))):
            self.__assignFitness()              # fitness assigned
            self.__deathRow()                   # weak indivs are killed
            while len(self.popPool) < self.size:
                self.__reproduce()                  # appends child to population
                        
        max_fit = 0.0
        max_agent = None

        for i in range(len(self.popPool)):
            max_fit = max(max_fit, self.popPool[i].getFitness())
            if self.popPool[i].getFitness() >= max_fit:
                max_agent = i

        #WingVis().visualize(self.popPool[max_agent].getGenes())
        WingVis().visualize(self.popPool[max_agent].getGenes(), self.fitnessMatrix)
        GraphVis().visualize(self.popPool[max_agent].getGenes(), self.fitnessMatrix)


        