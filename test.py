from DataPrep import createPopulation
from Requirements import calc_fitness,testPopulation,sort,merge
from Evolution import evolve

population = createPopulation()

e = evolve(population)

# fe = calc_fitness(e)
# a = evolve([e,fe])
# fa = calc_fitness(a)
# b = evolve([a,fa])
# fb = calc_fitness(a)
# c = evolve([b,fb])
# print(c)

def f(d):
    f = []
    p = []
    for k,v in d.items():
        f.append(k)
        p.append(v)

    m = merge([f,p])
    return m[0]
# list1 = d.keys()
# list2 = d.values()
# list = [list1,list2]
# m = merge(list)

# fit = calc_fitness(e)
# print(fit)
# list = [e,fit]
# print(evolve(list))

for i in range(100):
    temp = e
    ft = calc_fitness(temp)
    _2d = [temp,ft]
    e = evolve(_2d)
    d = sort(_2d)
    print(f(d))
print("---------------------------------------------------------1111111111111")
e2 = evolve(population)
for i in range(100):
    temp = e2
    ft = calc_fitness(temp)
    _2d = [temp,ft]
    e2 = evolve(_2d)
    d = sort(_2d)
    print(f(d))
print("---------------------------------------------------------2222222222222")
e3 = evolve(population)
for i in range(100):
    temp = e3
    ft = calc_fitness(temp)
    _2d = [temp,ft]
    e3 = evolve(_2d)
    d = sort(_2d)
    print(f(d))
print("---------------------------------------------------------333333333333333")
e4 = evolve(population)
for i in range(50):
    temp = e4
    ft = calc_fitness(temp)
    _2d = [temp,ft]
    e4 = evolve(_2d)
    d = sort(_2d)
    print(f(d))