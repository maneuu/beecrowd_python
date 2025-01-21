n = int(input())  # Número de medições
v = list(map(int, input().split()))  # Lista de velocidades
q = False  # Indica se houve queda
for i in range(1, n):
    if v[i] < v[i-1]:  # Verifica queda
        q = True
        break
print(i+1 if q else 0)  # Índice da primeira queda ou 0
