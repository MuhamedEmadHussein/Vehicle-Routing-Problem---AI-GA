from DataPrep import createPopulation
from Requirements import calc_fitness,sort,merge
from Evolution import evolve

population = createPopulation()

e = evolve(population)

def represent(dict):
    fit = []
    ind = []
    for k,v in dict.items():
        fit.append(k)
        ind.append(v)

    m = merge([fit,ind])
    print(m[0])

for i in range(100):
    temp = e
    ft = calc_fitness(temp)
    _2d = [temp,ft]
    e = evolve(_2d)
    dict = sort(_2d)
    represent(dict)


