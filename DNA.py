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

    def generate_genes(self, DNA_LENGTH):
        self.genes = []
        for i in range(0, DNA_LENGTH):
            gene = self.getChar()
            self.genes.append(gene)

    def getChar(self):
        chars_pool = string.printable
        char = chars_pool[random.randint(0, len(chars_pool) - 1)]
        return char
