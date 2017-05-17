import string
import random


class DNA:

    def __init__(self, DNA_LENGTH):
        self.generate_genes(DNA_LENGTH)

    def generate_genes(self, DNA_LENGTH):
        chars_pool = string.printable
        self.genes = []
        for i in range(0, DNA_LENGTH):
            gene = chars_pool[random.random(0, len(chars_pool))]
            self.genes.append(gene)