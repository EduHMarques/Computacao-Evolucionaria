def retorna_possibilidades(estado):
    possibilidades = []
    missionarios = estado[0]
    canibais = estado[1]
    barco = estado[2]

    if barco == 1:
        for i in range(0,3):
            for j in range(0,3):
                num_missionarios = missionarios - i
                num_canibais = canibais - j
                if i + j <= 2 and i + j >= 1 and num_missionarios >= 0 and num_canibais >= 0 and num_missionarios <= 3 and num_canibais <=3 :
                    if num_missionarios != 0:
                        if num_missionarios>=num_canibais:
                            if (3 - num_missionarios) != 0:
                                if (3 - canibais + j) <= (3 - missionarios + i):
                                    possibilidades.append([num_missionarios, num_canibais,0])
                            else:
                                possibilidades.append([num_missionarios, num_canibais,0])
                    else:
                        possibilidades.append([num_missionarios, num_canibais,0])
    else:
        for i in range(0,3):
            for j in range(0,3):
                num_missionarios = missionarios + i
                num_canibais = canibais + j
                if i + j <= 2 and i + j >= 1 and num_missionarios >= 0 and num_canibais >= 0 and num_missionarios <= 3 and num_canibais <= 3:
                    if missionarios != 0:
                        if (3 - num_missionarios) != 0:
                            if (3 - canibais - j) <= (3 - missionarios - i) and num_missionarios >= num_canibais:
                                possibilidades.append([num_missionarios, num_canibais, 1])
                        else:
                            possibilidades.append([num_missionarios, num_canibais, 1])
                    else:
                        possibilidades.append([num_missionarios, num_canibais, 1])
    
    return possibilidades

def bfs(inicio, objetivo):
    fila = [[inicio]]

    print(f'Estado inicial: {fila}\n')

    estados_explorados = []
    while fila:
        solucao = fila[0]
        fila = fila[1:]
        estado_final = solucao[-1]

        # Checa se o estado_final da solução já foi explorado
        if estado_final in estados_explorados:
            continue

        # Checa cada possibilidade da soluçao temporaria
        for move in retorna_possibilidades(estado_final):
            if move in estados_explorados:
                continue
            fila.append(solucao + [move])
        
        # Adiciona o estado final na estrutura de estados já explorados
        estados_explorados.append(estado_final)

        # Checa se chegou no estado final
        if estado_final == objetivo: 
            break
    
    return solucao

if __name__ == "__main__":

    estado_inicial = [3,3,1]
    objetivo = [0,0,0]

    resposta = bfs(estado_inicial, objetivo)
    count = 0
    for estado in resposta:
        print(f'Passo: {count}')
        print(f'Missionários: {estado[0]} | Canibais: {estado[1]}' )
        print(f'Barco: {estado[2]}\n', )

        count+=1