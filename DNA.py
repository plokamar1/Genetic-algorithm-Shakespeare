import string
import random


class DNA:

    def __init__(self,  DNA_LENGTH, target, genes=None):
        if genes == None:
            self.generate_genes(DNA_LENGTH)
        elif genes != None:
            self.genes = genes
        self.target = target
        self.DNA_LENGTH = DNA_LENGTH



    def generate_genes(self, DNA_LENGTH):
        self.genes = []
        for i in range(0, DNA_LENGTH):
            gene = self.getChar()
            self.genes.append(gene)

    def getChar(self):
        chars_pool = string.printable
        char = chars_pool[random.randint(0, len(chars_pool) - 1)]
        return char

    def get_fitness(self):
        i = 0
        fit_points = 0
        for gene in self.genes:
            if(gene == self.target[i]):
                fit_points += 1
            i += 1
        self.fit_points = int((fit_points/self.DNA_LENGTH )* 100)
        return(self.fit_points)

    def crossover(self, parentB):
        childGenes = []
        randomLocation = random.randint(0, len(self.target))
        for cnt in range(0, randomLocation):
            childGenes.append(self.genes[cnt])
        parentGenes = parentB.get_genes()
        for cnt in range(randomLocation, self.DNA_LENGTH):
            childGenes.append(parentGenes[cnt])
        
        child = DNA(self.DNA_LENGTH, self.target, childGenes)
        return child

    
    def mutate(self, mutationRate):
        for cnt in range(0, self.DNA_LENGTH):
            if(random.random()< mutationRate):
                self.genes[cnt] = self.getChar()


    def get_genes(self):
        return(self.genes)
