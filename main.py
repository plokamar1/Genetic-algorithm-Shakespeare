from Population import *

if __name__ == "__main__":
    populationNumber = 500
    Goal = 'O papas o paxys efage paxia fakh, giati papa paxy efages paxia fakh?'
    mutationRate = 0.01

    pops = Population(populationNumber, Goal, mutationRate)
    res = pops.generate()
    print(res)
