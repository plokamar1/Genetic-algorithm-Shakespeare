from Population import *

if __name__ == "__main__":
    populationNumber = 200
    Goal = 'To be or not to be.'
    mutationRate = 0.01

    pops = Population(populationNumber, Goal, mutationRate)
    pops.populate()
    pops.get_fitness()
    res = pops.generate()
    print(res)
