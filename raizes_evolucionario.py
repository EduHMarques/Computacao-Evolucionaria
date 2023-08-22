import random
import math

SIZE = 100
N_REP = 100

EQ = {'a': 1, 'b': -7, 'c': 0} # ax² + bx + c

def delta(eq):
    return pow(eq['b'], 2) - (4 * eq['a'] * eq['c'])

def bhaskara(eq):
    d = delta(eq)

    x1 = (-eq['b'] + math.sqrt(d)) / (2 * eq['a'])
    x2 = (-eq['b'] - math.sqrt(d)) / (2 * eq['a']) 

    return (x1, x2)

def gen_pop():
    pop = [(round(random.uniform(-10, 10),2),round(random.uniform(10, 10),2)) for _ in range(SIZE)]

    return pop

def fitness(z, t, eq):
    fit1 = (eq['a'] * pow(z, 2)) + (z * eq['b']) + eq['c']
    fit2 = (eq['a'] * pow(t, 2)) + (t * eq['b']) + eq['c']

    fit1 = abs(fit1)
    fit2 = abs(fit2)

    return round((fit1 + fit2)/2, 2)

def torneio(pop):
    nova_pop = []

    for ind in pop:
        torneio = random.sample(pop, 2)
        melhor_individuo = []
        melhor_fit = 100000
        for i in torneio:
            fit = fitness(ind[0], i[1], EQ)
            if fit < melhor_fit:
                melhor_fit = fit
                melhor_individuo = i
        nova_pop.append(melhor_individuo)

    return nova_pop

def mutation(pop):
    for i in range(len(pop)):
        
        r = random.randint(0, 100)
        if r >= 70:
            a, b = pop[i]

            v = random.uniform(-2, 2)

            fit1 = fitness(a, a, EQ)
            fit2 = fitness(b, b, EQ)

            if fit1 <= 0.5 and fit2 <= 0.5:
                continue

            pos = random.randint(0, 1)

            if pos == 0:
                pop[i] = (a+v, b)
            else:
                pop[i] = (a, b+v)

    return pop

if __name__ == '__main__':
    pop = gen_pop()

    print("População Inicial:")
    print(pop)
    
    overall_fitness = [fitness(ind[0], ind[1], EQ) for ind in pop]

    for _ in range(N_REP):
        pop = torneio(pop)
        pop = mutation(pop)
        overall_fitness = [fitness(ind[0], ind[1], EQ) for ind in pop]

    pop = [(round(ind[0], 2), round(ind[1], 2)) for ind in pop] # Arredonda os resultados para 2 casas decimais

    print(f"\nPopulação após {N_REP} repetições:")
    print(pop)

    print(f"\nSolução ótima: {bhaskara(EQ)}\nMelhor indivíduo encontrado: {pop[0]}")