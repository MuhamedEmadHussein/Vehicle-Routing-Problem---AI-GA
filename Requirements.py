from random import randint, sample
import pandas as pd

# Evolution Requirements
def getCities(parents):
    cities = list(parents[0][0].replace(" ",""))
    # cities.append('#')
    return cities

def filterCities(child , cities):
    copy = cities.copy()
    for x in cities:
        if x in child:
            copy.remove(x)
    return copy

def reflect(str):
    s = []
    
    c = 0
    for i in range(len(str)):
        if str[i] == ' ':
            s.append(str[c:i])
            s.append(str[i])
            c = i+1
    s.append(str[c:])

    length = len(s)
    r1 = randint(0,length-1)
    r2 = randint(0,length-1)

    s[r1] = s[r1][::-1]
    s[r2] = s[r2][::-1]

    return ''.join(s)

def swap(str,r1,r2):
    l = list(str)
    c1 = str[r1]
    c2 = str[r2]
    if c1==" ":
        r1 += 1
        c1 = str[r1]
    if c2==" ":
        r2 += 1
        c2 = str[r2]
    l[r1] = c2
    l[r2] = c1
    return ''.join(l)

def includeParents(parents):
    population = []

    oldParents = []
    for i in range(len(parents)):
        for j in range(2):
            oldParents.append(parents[i][j])
    
    for x in oldParents:
        population.append(x)
    
    return population

def includeRands(pop , rands):
    for x in rands:
        pop.append(x)
    return pop


def testPopulation(pop,cities):
    f = 0
    for x in pop:
        for i in range(len(cities)-1):
            if x.count(cities[i]) != 1 or cities[i] == '#':
                f += 1
                print(x,' ',cities[i])
    print(f'{f} faliure')


# Selection Requirements
def sort(population):
    d = {}
    for i in range(len(population[0])):
        d[str(population[1][i])] = population[0][i]
    d = dict(sorted(d.items(),reverse=True))
    return d

def filterPopulation(population):
    dict = sort(population)
    populationList = []

    for v in dict.values():
        populationList.append(v)
        
    return populationList

def createRoullet(population):
    populationList = filterPopulation(population)
    sum = 0
    for j in range(0, len(populationList)):
        sum += 1 / (j + 1)
    return sum

# Data Preparation Requirements
def startNode():
    x = 200
    y=100
    Direct = [x,y]
    return Direct

def get_cities():
    df = pd.read_excel (r'data.xlsx')
    locations = []
    for i in range(len(df['x'])):
        locations.append(df['city'][i])
    return locations

def get_coordinates():
    df = pd.read_excel (r'data.xlsx')
    coordinates = []
    for i in range(len(df['x'])):
        coordinates.append([df['x'][i], df['y'][i]])    
    return coordinates

def create_dictionary():
    cities = get_cities()
    coordinates = get_coordinates()
    map = {}
    map["Start"] = startNode()
    for i in range(len(cities)):
        map[cities[i]] = coordinates[i]
    return map

def calc_distance(x1, y1, x2, y2):
   return ( ((x2 - x1 )**2) + ((y2-y1)**2) )**0.5

def calc_cost(population):
    dict = create_dictionary()
    individual = {}
    cost = 2

    c = 0
    for x in population:
        individual[c] = x.split()
        c += 1

    sum = 0
    totalCost = []
    for v in individual.values():
        
        for x in v:

            for j in range(len(x)):

                if j == 0 or j == len(x)-1:
                    x1 = dict['Start'][0]
                    y1 = dict['Start'][1]
                    x2 = dict[x[j]][0]
                    y2 = dict[x[j]][1]
                    dist = calc_distance(x1, y1, x2, y2)
                    sum += dist
                    continue

                x1 = dict[x[j]][0]
                y1 = dict[x[j]][1]
                x2 = dict[x[j-1]][0]
                y2 = dict[x[j-1]][1]
                dist = calc_distance(x1, y1, x2, y2)
                sum += dist

        totalCost.append(int(sum) * cost)
        sum = 0
    return totalCost

def calc_fitness(population,target=30000):
    fit = []
    total = calc_cost(population)
    for x in total:
        fit.append(target - x)
    return fit

def merge(list):
    newlist = list.copy()
    for i in range(len(list[0])):
        newlist[0][i] += ' ' + str(newlist[1][i])
    del newlist[1]
    newlist = newlist[0]
    return newlist