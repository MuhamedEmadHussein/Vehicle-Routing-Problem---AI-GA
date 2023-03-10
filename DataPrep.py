import pandas as pd
import random
from Requirements import get_cities, calc_fitness


def createPopulation():
    population = []
    cities = get_cities()
    truckNum = 6

    for i in range(100):
        cities = random.sample(cities, len(cities))

        individual = []

        for z in range(truckNum):
            individual.append(" ")

        c=0
        for x in range(len(cities)):
            if(c==truckNum):
                c=0
            individual[c] += cities[x]
            c+=1

        individual = ''.join(individual)

        population.append(individual.strip())

    fit = calc_fitness(population)
    return [population,fit]

