import random as rand
from Requirements import filterPopulation,createRoullet

# population = ["ABCDF 7", "GHKLM 8", "BACFD 6", "BCASQ 2", "HKGML 10", "UYLMX 1", "PONMZ 4", "WTOLR 3"]
# population = createPopulation()
# population = merge(createPopulation())

# length = len(population[0])
# print(length)

def selection(population, retain=0.30, random_select=0.20):
    length = len(population[0])
    population_List = []
    sortedRankedList = filterPopulation(population)

    best_rated = round(length * retain)
    # print("number of best populations",best_rated)
    sum = createRoullet(population)

    for k in range(0, (2 * best_rated)):
        flag = 0
        sumOfProb = 0
        for n in range(0, best_rated):
            if flag == 0:
                random = rand.randint(0, 100)

            sumOfProb += (1 / (n + 1) * 1 / sum) * 100

            if (sumOfProb > random):
                population_List.append(sortedRankedList[n])
                # print("best populations selected : ",population_List)
            else:
                flag = 1

    random_parents = round(length * random_select)
    randomPopList = []
    list = sortedRankedList[best_rated + 1: len(sortedRankedList)]
    for j in range(0, random_parents):
         #print("random index : ",j)
         #print("random individual selected :",sortedRankedList[j])
         if(len(randomPopList)<=random_parents):
             try:
                randomPopList.append(list[j])
             except IndexError:
                 continue

    bestPopulationList = []

    # filter best population without repetition of parents

    for x in range(2, len(population_List), 2):

        if population_List[x - 2] != population_List[x - 1]:
            mylist = [population_List[x - 2], population_List[x - 1]]
            reversed = [population_List[x - 2], population_List[x - 1]]
            reversed.reverse()
            if mylist not in bestPopulationList and reversed not in bestPopulationList:
                bestPopulationList.append([population_List[x - 2], population_List[x - 1]])

    # population List with final form
    newPopulationList = []
    if(len(bestPopulationList)-retain*100 > 0) :
        newPopulationList = [bestPopulationList[0:int(retain*100)], randomPopList]
    else:
        newPopulationList = [bestPopulationList, randomPopList]


    # print(len(newPopulationList[0]))
    # print(len(newPopulationList[1]))
    return newPopulationList



# print(selection())



