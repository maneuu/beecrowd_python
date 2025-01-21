def calcular_hora_chegada(S, T, F):
    # Calcula a hora de chegada
    hora_chegada = S + T + F
    
    # Ajusta se a hora de chegada for 24 ou mais
    if hora_chegada >= 24:
        hora_chegada -= 24
    elif hora_chegada < 0:
        hora_chegada += 24
    
    return hora_chegada

# Leitura da entrada
S, T, F = map(int, input().split())

# Chama a função para calcular a hora de chegada
print(calcular_hora_chegada(S, T, F))
