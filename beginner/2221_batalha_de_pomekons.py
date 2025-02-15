casos = int(input())
for _ in range(casos):
    resultado = []
    bonus = int(input())
    for _ in range(2):
        Ataque,Defesa,Level = [int(N) for N in input().split()]
        if Level % 2 == 0:
            ValorGolpe = bonus + (Ataque+Defesa)/2
        else:
            ValorGolpe = (Ataque+Defesa)/2
        resultado.append(ValorGolpe)
    if resultado[0] > resultado[1]:
        print("Dabriel")
    elif resultado[0] < resultado[1]:
        print("Guarte")
    else:
        print("Empate")
        