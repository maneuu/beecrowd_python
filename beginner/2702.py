pratos = [int(X) for X in input().split()] #Frango, Bife, Massa
passageiros = [int(x) for x in input().split()]

resultado = 0
for i in range(3):
    diferenca = pratos[i] - passageiros[i]
    if diferenca < 0:
        resultado += (diferenca) * (-1)

print(resultado)