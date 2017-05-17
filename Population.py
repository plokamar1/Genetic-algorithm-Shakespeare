from DNA import *

class Population:
    def __init__(self, TotalPopulation, target):
        self.population = []
        self.target = target
        for i in range(0,TotalPopulation):
            self.population.append(DNA(len(target)))
    