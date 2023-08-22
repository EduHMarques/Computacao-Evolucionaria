import random

# Representação da melhor solução = [(0, 2, 0, 0), (0, 0, 0, 1), (0, 2, 0, 0), (0, 0, 0, 1), (2, 0, 0, 0), (0, 0, 1, 1), (2, 0, 0, 0), (0, 0, 0, 1), (0, 2, 0, 0), (0, 0, 0, 1), (0, 2, 0, 0)]

def apt(movimentos):
    missionarios = 3
    canibais = 3

    for move in movimentos:
        missionarios -= move[0] - move[2]
        canibais -= move[1] - move[3]

        if (missionarios < canibais and (abs(missionarios - 3) < abs(canibais - 3))):
            return -1
        if (missionarios > 3 or canibais > 3 or missionarios < 0 or canibais < 0):
            return -1
        
    return (6 - missionarios - canibais)


def printa_solucao(movimentos):
    missionarios = 3
    canibais = 3

    for move in movimentos:
        missionarios -= move[0] - move[2]
        canibais -= move[1] - move[3]

        print(f'Inicio: {missionarios}|{canibais}, Fim: {abs(missionarios - 3)}|{abs(canibais - 3)}')
    
    
def movimentos(lado):
    moves = []
    # Indo
    if lado == 0:
        moves.append((1, 0, 0, 0))
        moves.append((1, 1, 0, 0))
        moves.append((2, 0, 0, 0))
        moves.append((0, 1, 0, 0))
        moves.append((0, 2, 0, 0))
    #Voltando
    if lado == 1:
        moves.append((0, 0, 1, 0))
        moves.append((0, 0, 1, 1))
        moves.append((0, 0, 2, 0))
        moves.append((0, 0, 0, 1))
        moves.append((0, 0, 0, 2))

    return random.choice(moves)

def gera_individuo():
    estados = random.randint(5, 15)
    individuo = []

    while estados > 0:
            individuo.append(movimentos(len(individuo) % 2))
            if (apt(individuo) == -1):
                individuo.pop()
                continue
            estados -= 1

    return individuo

# Gera população
def initial_population(num_individuos): 
    return [gera_individuo() for _ in range(num_individuos)]

def mutacao(populacao):
    for i in range(len(populacao)):
        r = random.randint(0, 100)

        if r >= 60:                         # Chance de mutar 40%
            if (apt(populacao[i]) != 6):
                while True:
                    populacao[i].append(movimentos(len(populacao[i]) % 2))
                    if (apt(populacao[i]) != -1):
                        break
                    else:
                        populacao[i].pop()

    return populacao

def ordernacao(pop, num_individuos):
    fitness = [apt(p) for p in pop]
    sorted_pop = [(pop[i], fitness[i]) for i in range(len(pop))]
    sorted_pop.sort(key=lambda s: s[1], reverse=True)
    sorted_pop = [i[0] for i in sorted_pop]

    return sorted_pop[:num_individuos]

def selecao(pop, num_individuos):

    deletados = 0
    for i,ind in enumerate(pop):
        if (len(ind) > 20):
            pop.pop(i)
            deletados += 1

    for i in range(deletados):
        pop.append(gera_individuo())

    pop = ordernacao(pop, num_individuos)

    return pop

if __name__ == "__main__":

    # Melhor aptidão: 6

    populacao = initial_population(10)
    maiorAptidao = 0
    rep = 0

    while rep < 250:
        for i in range(len(populacao)):
            if apt(populacao[i]) == 6:
                maiorAptidao = apt(populacao[i])

        populacao = selecao(populacao, 10)
        populacao = mutacao(populacao)
        
        rep += 1
        print(f'Geração: {rep}')

    print(f'\nPopulacao apos {rep} repeticos: ')
    for i in range(len(populacao)):
        print(f'Individuo: {i+1} - Função aptidao: {apt(populacao[i])}')

    print('\nSolução do melhor indivíduo:')
    printa_solucao(populacao[0])