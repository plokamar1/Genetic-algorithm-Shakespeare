from DNA import *

class Population:
    def __init__(self, TotalPopulation, target, mutationRate):
        self.fitness = []
        self.population = []
        self.target = target
        self.TotalPopulation = TotalPopulation

        self.populate()
        self.get_fitness()

    def populate(self):
        self.population = []
        for i in range(0, self.TotalPopulation):
            self.population.append(DNA(len(self.target), self.target))

    def get_fitness(self):
        for individual in self.population:
            self.fitness.append(individual.get_fitness())
        
    