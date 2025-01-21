
N = int(input())

if N: # N = n != 0
    denominador = 0
    fracoes = []
    for _ in range(N):
        fracoes.append(1/(6 + denominador))
        denominador = fracoes[-1]
    fracao = fracoes[-1]
else: # N = 0
    fracao = 0

formula = 3 + fracao
print(f"{formula:.10f}")