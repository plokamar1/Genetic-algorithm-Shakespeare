from DNA import *


class Population:
    def __init__(self, TotalPopulation, target, mutationRate):
        self.fitness = []
        self.population = []
        self.target = target
        self.mutationRate = mutationRate
        self.TotalPopulation = TotalPopulation
        self.generation = 0
        self.FinalScore = 100
        self.populate()

    def populate(self):
        self.population = []
        for i in range(0, self.TotalPopulation):
            self.population.append(DNA(len(self.target), self.target))
        self.gather_fitness()

    def gather_fitness(self):
        for individual in self.population:
            self.fitness.append(individual.get_fitness())

    def generate(self):
        found = None
        while found == None:
            self.bucket = []
            cnt = 0
            #Create bucket with parents
            if max(self.fitness) == 0:
                self.bucket = self.population
            else:
                for individual in self.population:
                    for i in range(0, self.fitness[cnt]+1):
                        self.bucket.append(individual)
                    cnt += 1
            self.population = []
            self.fitness = []

            #choose random parents to make a new child with their genes
            for cnt in range(0, self.TotalPopulation):
                RandomEntry = random.randrange(0, len(self.bucket))

                randParentA = self.bucket[RandomEntry]

                RandomEntry = random.randrange(0, len(self.bucket))

                randParentB = self.bucket[RandomEntry]
                child = randParentA.crossover(randParentB)
                child.mutate(self.mutationRate)
                self.fitness.append(child.get_fitness())
                self.population.append(child)
                print(''.join(child.get_genes()) + ' ' +str(child.get_fitness()) + ' ' + str(self.generation)+' '+str(len(self.bucket))+' '+str(max(self.fitness)))
            if self.FinalScore in self.fitness:
                indexNum = self.fitness.index(self.FinalScore)
                found = self.getResult(self.population[indexNum])
                return found
            self.generation += 1

    def getResult(self, child):
        result = {'String':''.join(child.get_genes()),'Fitness':child.get_fitness(),'Generation':self.generation}
        return result
