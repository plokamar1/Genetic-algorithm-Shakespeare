from DNA import *


class Population:
    def __init__(self, TotalPopulation, target, mutationRate):
        self.fitness = []
        self.population = []
        self.target = target
        self.mutationRate = mutationRate
        self.TotalPopulation = TotalPopulation
        self.generation = 0

    def populate(self):
        self.population = []
        for i in range(0, self.TotalPopulation):
            self.population.append(DNA(len(self.target), self.target))
        print('Initial population created')
            #print(self.population[i].get_genes())

    def get_fitness(self):
        for individual in self.population:
            self.fitness.append(individual.get_fitness())
        
    def generate(self):
        found = None
        while found == None:
            self.bucket = []
            cnt = 0
            #Create bucket with parents
            for individual in self.population:
                for i in range(0, self.fitness[cnt]):
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
                print(''.join(child.get_genes()) + ' ' +str(child.get_fitness()) + ' ' + str(self.generation)+' '+str(len(self.bucket)))
            if 100 in self.fitness:
                indexNum = self.fitness.index(100)
                found = self.getResult(self.population[indexNum])
                    return found
            self.generation += 1
            #print(self.generation)

    def getResult(self, child):
        result = {'String': ''.join(child.get_genes()), 'Fitness': child.get_fitness(
        ), 'Generation': self.generation}
        return result

