from DNA import *

class Population:
    def __init__(self, TotalPopulation, target):
        self.population = []
        self.target = target

        self.populate()
    def populate(self):
        self.population = []
        for i in range(0, self.TotalPopulation):
            self.population.append(DNA(len(self.target), self.target))
    