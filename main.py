from Population import *

if __name__ == "__main__":
    populationNumber = 200
    Goal = 'I am a little unicorn'
    mutationRate = 0.01
    
    pops = Population(populationNumber, Goal, mutationRate)
    result = pops.generate()
