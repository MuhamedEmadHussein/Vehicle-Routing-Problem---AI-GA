from Selection import selection
from Requirements import getCities,filterCities,reflect,swap,includeParents,includeRands, testPopulation
from random import randint
from DataPrep import createPopulation

pop = createPopulation()

# s = selection(0.20, 0.20)
# p = s[0]
# cities = getCities(p)

def crossOver(parents,randIndividuals,cities):

    population = includeParents(parents)
    for x in parents:

        parent1 = x[0]
        parent2 = x[1]
        
        r = randint(1 , len(x[0])-1)

        child1 = parent1[:r]
        child2 = parent2[:r]

        for i in range(r,len(parent1)):
            if parent2[i] not in child1:
                child1 += parent2[i]
            elif parent2[i] != ' ':
                child1 += '*'
            else:
                child1 += parent2[i]
            
            if parent1[i] not in child2:
                child2 += parent1[i]
            elif parent1[i] != ' ':
                child2 += '*'
            else:
                child2 += parent1[i]

        cities1 = filterCities(child1,cities)
        cities2 = filterCities(child2,cities)

        list1 = list(child1)
        list2 = list(child2)

        for x in range(r,len(child1)):
            if child1[x] == '*':
                c = cities1[0]
                list1[x] = c
                cities1.remove(c)

            if child2[x] == '*':
                c = cities2[0]
                list2[x] = c
                cities2.remove(c)

        child1 = ''.join(list1)
        child2 = ''.join(list2)

        population.append(child1)
        population.append(child2)

    population =  includeRands(population , randIndividuals)

    return population
    
def mutate(population):
    i_len = len(population[0])
    r1 = randint(1,len(population)-1)
    r2 = randint(1,len(population)-1)

    for i in range(min(r1,r2),max(r1,r2)):
        # r1 = randint(0,i_len-1)
        # r2 = randint(0,i_len-1)
        s = population[i]
        # s = swap(s,r1,r2)
        s = reflect(s)
        population[i] = s

    return population

def evolve(population):
    selected = selection(population,0.20, 0.20)
    parents = selected[0]
    randIndividuals = selected[1]
    cities = getCities(parents)

    population = crossOver(parents,randIndividuals,cities)
    
    mutate(population)
    
    return population


